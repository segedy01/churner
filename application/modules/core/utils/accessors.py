"""
Resolvers hold the core of the resolution utilities to promote code reuse
"""
import re
from collections import deque
from collections import OrderedDict

from redis.exceptions import ConnectionError

from application import rdb
from application.constants import REDIS_AUTH_TOKEN_PREFIX
from application.constants import SERVER_ERROR_ALTERNATE_MESSAGE

from flask import g

from application.modules.core.logger import message_logger, logger
from application.modules.core.exc.failed import ServiceUnavailableError, ServiceNotFoundError
from application.modules.core.exc.missing import UserNotFoundError, MissingResourceError
from application.modules.core.exc.missing import MissingHeaderException, MissingParametersError, CredentialNotFoundError


ACTIONS = {
    "create": 1,
    "modify": 2,
    "view": 3,
    "delete": 4
}
ACTIONS_MAP = {
    "post": "create",
    "get": "view",
    "put": "modify",
    "patch": "edit",
    "delete": "delete"
}


def check_authentication_token_in_redis(application_client_id, authentication_token=None):
    """
    Checks to see if such an authentication token is stored in the internal key-value store in this case: `redis`

    This method not only checks redis but resaves to redis should the credential not exist in redis but remain valid
    after the TTL set in redis has expired and out of commission

    :param authentication_token:        The bare bones authentication token free from any prefixes or addendums
                                        for deserialization and operation in redis
                                        :type <type, 'str'>
    :param application_client_id:       The client id passed in with the client request, and used to map to a user
                                        in redis
    :return valid_token:                Boolean value stipulating the validity of the authentication token based on
                                        the context provided with the client request
                                        :type <type, 'bool'>
    """
    #: redis_hash_name = REDIS_AUTH_TOKEN_PREFIX + authentication_token
    try:
        client_token = rdb.get(application_client_id)
    except ConnectionError as e:
        logger.error(message_logger("REDIS NOT AVAILABLE: " + e.message, client_token))
        return False
    if authentication_token:
        #: If an authentication_token is sent, then return a comparison
        #: If the names match then `we have a home run` return true or lazy true like below
        #: TODO: Implement save again if expired in redis -- DONE
        return client_token == authentication_token

    #: If the names match then `we have a home run` return true or lazy true like below
    #: TODO: Implement save again if expired in redis -- DONE
    return client_token




def has_privilege(credential, http_method, endpoint):
    #: get privileges from credential
    __privileges = credential.get("privileges")

    #: check to see if they have rights to the microservice/endpoint
    __orders = __privileges.get(endpoint, False)
    if not __orders:
        return __orders

    #: get the rights representation from the http method i.e. post = create, put = modify, patch = edit
    __action = ACTIONS_MAP.get(http_method.lower())
    __has_privilege = __orders.get(__action)
    return __has_privilege


def inspect_headers(http_request):
    """
    Inspects the incoming http request's headers to verify authenticity and validity of the request

    Looks for the authentication token and request to type to ensure that the request coming in is not only
    properly formatted but also useful or allowed to continue on to the fetchr services soup

    :param http_request:    The http request object that comes from the client with each request to
                            the fetchr endpoint. Request types must be json based or they will be
                            rejected :type <type, 'flask.Request'>
    :return:                 value representing minimal header requirements validity
                            :type <type, 'bool'>
    """
    #: logger.info('Route Resolve Header Called by IP Address: {}'.format(http_request.access_route))
    http_headers = http_request.headers
    wanted_mime = 'application/json'

    authorization = http_headers.get('Authorization') or http_headers.get('authorization')
    accept = http_headers.get('Accept') or http_headers.get('accept')

    if not authorization:
        raise MissingHeaderException("Authorization header not found")

    return {"authorization": authorization}


def inspect_json_body(http_request, required=None):
    """
    Inspects the incoming http request's headers to verify authenticity and validity of the request

    Looks for the authentication token and request to type to ensure that the request coming in is not only
    properly formatted but also useful or allowed to continue on to the fetchr services soup

    :param http_request:    The http request object that comes from the client with each request to
                            the fetchr endpoint. Request types must be json based or they will be
                            rejected :type <type, 'flask.Request'>
    :return:                 value representing minimal header requirements validity
                            :type <type, 'bool'>
    """
    #: NOTE: Extemely important assumption that json exists to prevent automatic flask bad request handling
    json_body = http_request.json
    if required:
        for item in required:
            present = json_body.get(item)
            if not present:
                raise MissingParametersError("{} is required but is missing".format(item))
    return json_body
