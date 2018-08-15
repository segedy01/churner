"""
Accessors

application.modules.core.utils
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Writes or persists to libraries files etc in the context of util methods
"""
from datetime import datetime as clock
from datetime import timedelta
import os
import random
import string

from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from application import rdb
from application.constants import REDIS_AUTH_TOKEN_PREFIX
from application.modules.core.logger import logger
from application.modules.core.exc.invalid import InvalidRequestError

_ALLOWED_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'UPDATE', 'DELETE']
_RANDOM_QUALIFIER = 3283018301392
_TIME_TO_LIVE = 3600 * 24 * 30 * 12 * 5
TOKEN_TIME_TO_LIVE = 15 * 60


_DELETE = 'DELETE'
_GET = 'GET'
_SECRET_KEY = 'th1si3aS3CRETk3y'

def generate_authentication_token(token_dictionary=None, time_to_live=None):
    """
    Generates an authentication token for use across the entire application
    by encoding the :param token_dictionary using an environmental variable read
    secret key

    :param token_dictionary:    The token dictionary to encode into an authentication
                                token
                                :type <type, 'str'>

    :return token:              The generated authentication token to return to the
                                calling context
                                :type <type, 'str'>
    """
    #: If time to live is none initialize to HH * 24H * 1MONTH * 1YEAR * 5YEARS... Why? Why Not
    time_to_live = time_to_live or _TIME_TO_LIVE

    #: Set created time and expiry time in epoch for easy integer comparisons directly
    if not token_dictionary:
        created_time = clock.now()
        expiry_time = clock.now() + timedelta(seconds=time_to_live)
        token_dictionary = {
            "created_time": str(created_time),
            "expiry_time": str(expiry_time)
        }

    SECRET_KEY = os.environ.get("SECRET_KEY") or _SECRET_KEY
    serializer = Serializer(secret_key=SECRET_KEY, expires_in=time_to_live)
    authentication_token = serializer.dumps(token_dictionary)
    return authentication_token


def generate_nonce():
    __key = ''.join(random.choice(string.ascii_letters) for index in range(7))
    __value = str(uuid4()).replace("-", "")
    return {__key: __value}


def token_date_encoder(obj):
    if isinstance(obj, clock):
        return obj.__str__()


def set_authentication_token_in_redis(authentication_token, application_client_id, time_to_live=None):
    """
    Saves the provided authentication token to the key-value store with a prefix i.e. `credential:token`

    Credential tokens are saved to a fast read write key value store to speed up authentication lookup
    and prevent deserialization on each request

    :param authentication_token:        The authentication token to persist to the key value store usually a
                                        TimedJsonWebSerializerSignature
                                        :type <type, 'str'>
    :param application_client_id:       The id of the client that owns this authentication token, extremely useful
                                        as it helps to identify the client which is everything when it comes to
                                        authorization using tokens
                                        :type <type, 'str'>
    :return:
    """
    #: add a prefix to the token to make it appear as `prefix:token`
    #: and provide clear collision free meta information as to its purpose as well
    #: redis_hash_name = REDIS_AUTH_TOKEN_PREFIX + authentication_token
    rdb.set(application_client_id, authentication_token)

    #: If time to live provided then expire the authentication token
    #: after that time has elapsed accordingly
    if time_to_live:
        rdb.expire(application_client_id, time_to_live)


def populate_self_from_json(model_instance, collection, exclusions=None):
    """
    Populate the class instance from a json dictionary if the keys in the
    json collection match the instance names

    :param model_instance:      The class instance to populate with values from the
                                collection where the key name matches the class attribute name
                                :type <type, type>

    :param collection:          Key value collection to use as data source for population of the
                                model instance.
                                :type <type, 'dict'>

    :param exclusions:          A list of attributes to exclude from the assignment operation. This acts
                                as a security mechanism to prevent unwanted assignment due to the introspective
                                nature of this method.
                                :type <type, 'list'>
    """
    #: enumerate collection at the same time as class
    #: check if the attribute exists in the class before assigning
    exclusions = exclusions or []
    for key in collection:
        attribute = getattr(model_instance, key, _RANDOM_QUALIFIER)
        if attribute == _RANDOM_QUALIFIER:
            continue

        is_method_therefore_skip = hasattr(attribute, '__call__') or key in exclusions
        if is_method_therefore_skip:
            continue

        setattr(model_instance, key, collection.get(key))
