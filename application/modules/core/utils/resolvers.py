"""
Utils mainly act as a holder of utility functions that expose a commonly
used actions to the modules to promote code reuse.

application.modules.core.utils
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from collections import deque, OrderedDict
import re
import os

from flask import current_app, g

from itsdangerous import BadSignature
from itsdangerous import BadTimeSignature
from itsdangerous import SignatureExpired
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from application.constants import AUTH_STRING_REGEX, AUTHENTICATION_TYPE
from application.constants import AUTH_REGEX, FILTER_COLLECTION, NOT_EMPTY, NO_SPACE, NO_NUMBER, NO_SYMBOL
from application.constants import HAS_CAPS, HAS_EMPTY, HAS_LENGTH, HAS_NUMBER, HAS_SPACE, HAS_SYMBOL
from application.constants.messages.error import *
from application.modules.core.exc.failed import DuplicateResourceError
from application.modules.core.exc.invalid import InvalidParametersError, InvalidValueError, InvalidCredentialsError
from application.modules.core.exc.missing import MissingResourceError, MissingParametersError, CredentialNotFoundError

from application.modules.core.logger import logger


__POST = 'post'
__PUT = 'put'
__ALLOWED_METHODS = [__POST, __PUT]
_SECRET_KEY = 'th1si3aS3CRETk3y'


def check_for_clients(provider, order_id):
    """
    Gets the client instance with the corresponding
    :param `order_id` and 'provider_id' by checking if the order exists and returning an instance if it does
    and raising an `application.modules.core.exceptions.InvalidOrderError` error if it does not
    exist.

    :param provider:        valid 3PL provider object from 'CourierProvider' Class
                            :type <type, 'str'>

    :param order_id:        The order_id  which will get from the 3PL request
                            :type <type, 'str'>

    :return:                checks for order exists or not
                            :type <type, 'object'>
    """
    try:
        check_for_services = Order.objects(provider_id=provider, order_id=order_id)
        if len(check_for_services) == 0:
            raise MissingResourceError("Order with a matching id could not be found")
        return check_for_services.first()
    except Exception as e:
        raise MissingResourceError("The Resource Is Not Part Of Our System")


def deserialize_token(token, caller=None):
    """
    Deserialilze the token using the secret key of the application

    :param token:       The token to be deserialized.
                        :type <type, 'itsdangerous.TimedJSONWebSignatureSerializer'>

    :param caller:      The calling context or origin of the deserialization request
                        :type <type, 'str'>
    """
    SECRET_KEY = os.environ.get("SECRET_KEY") or _SECRET_KEY
    serializer = Serializer(secret_key=SECRET_KEY)

    caller = caller or "Unknown Client"

    try:
        valid_data = serializer.loads(token)
    except (BadTimeSignature, BadSignature) as e:
        #: log exception here
        logger.error('%s Called Verify Credential Token: %s' % (caller, e.message))
        raise CredentialNotFoundError("Open sesame does not work here")
    except SignatureExpired as e:
        logger.error('%s Called Verify Credential Token: %s' % (caller, e.message))
        raise InvalidCredentialsError("Ask us for new credentials")
    return valid_data


def required_fields_present(required_fields, json_payload):
    """
    Checks that the :param required_fields are present in the :param json_payload collection recursively
    by calling the :meth get_dictionary_values_using_nested_list.

    If a value is not found then the parent and the field if nested is injected into a friendly error
    message to provide clarity to the calling context on the cause of the MissingParametersError.

    :param required_fields:     Collection of keys that should be validated for being present.
                                :type <type, 'list'>

    :param json_payload:        Key value collection to inspect for the presence of the wanted fields.
                                :type <type, 'dict'>
    :return:
    """
    from application.modules.core.utils.converters import get_dictionary_value_using_nested_list
    for key_map in required_fields:
        try:
            value = get_dictionary_value_using_nested_list(key_map, json_payload)
        except KeyError as e:
            value = None

        if value==None:
            missing_value = key_map.pop()
            parent_value = key_map.pop() if key_map else "Sorry"
            raise MissingParametersError("{} {} is a required json field".format(parent_value, missing_value))


def resolve_authentication_string(full_authentication_token):
    """
    Resolves the authentication string parsed from the Authorization header of an http_request

    Different authorization schemes exist unfortunately, this function parses the strings into
    internally representable formats for easy retrieval by interested callers

    :param full_authentication_token:       authentication string as retrieved from the
                                            Authorization header
                                            :type <type, 'str'>
    :return authentication_token:           Resolved authentication token without its metadata
                                            :type <type, 'str'>
    """

    #: Ensure full_authentication_token is of the right format
    compiled_auth_token_regex = re.compile(AUTH_STRING_REGEX)
    if not compiled_auth_token_regex.match(full_authentication_token):
        raise InvalidCredentialsError("Invalid token")

    #: Split on the first space ` ` to get the auth type away from the auth string
    authentication_type, authentication_string = full_authentication_token.split(' ', 1)

    if not authentication_type == AUTHENTICATION_TYPE:
        raise InvalidCredentialsError("Authorization token has invalid Bearer identifier")

    return authentication_string


def resolve_authentication_token(full_authentication_token):
    """
    Resolves the authentication string parsed from the Authorization header of an http_request

    Different authorization schemes exist unfortunately, this function parses the strings into
    internally representable formats for easy retrieval by interested callers

    :param full_authentication_token:       authentication string as retrieved from the
                                            Authorization header
                                            :type <type, 'str'>
    :return authentication_dictionary:      Resolved collection holding the token and other
                                            artifacts of the authorization string depending on
                                            the authorization protocol and type
                                            :type <type, 'dict'>
    """
    authentication_dictionary = OrderedDict()

    #: Ensure full_authentication_token is of the right format
    compiled_auth_token_regex = re.compile(AUTH_REGEX)
    if not compiled_auth_token_regex.match(full_authentication_token):
        raise InvalidCredentialsError("Invalid token")

    #: Split on the first space ` ` to get the auth type away from the auth string
    authentication_type, authentication_string = full_authentication_token.split(' ', 1)

    #: Split on the first `:` to separate and get the user id
    #: away from the auth token as the user does not use such a symbol
    user_id, authentication_token = authentication_string.split(':', 1)

    #: assign the resolved values to the returnable collection
    authentication_dictionary['authentication_type'] = authentication_type
    authentication_dictionary['user_id'] = user_id
    authentication_dictionary['token'] = authentication_token

    return authentication_dictionary


def resolve_request_params(http_request):
    """
    Resolves the request got from the client. If failed then an error is raised with the appropriate code.

    :param http_request:        The http request gotten from the client
                                :type <type, 'flask.wrappers.Request'>
    :return request_params:     A key value collection to use as part of internal request.
                                :type <type, 'dict'>
    """
    params = {}
    try:
        the_method = http_request.method.lower()
        if the_method in __ALLOWED_METHODS:
            return http_request.json
        if http_request.method == 'GET' or http_request.method == 'DELETE':
            return http_request.headers
    except Exception as e:
        logger.error(e)
        raise InvalidParametersError

    return params


def resolve_request_url(http_url):
    """
    Resolves the url to an internally represented service name and prepares it for re-dispatching

    When a url comes in it is automatically parsed and sent to this function to be resolved into
    the appropriate internal request
    This has nothing to do with authentication

    :param http_url:        The url to be resolved :type <type, 'str'>
    :return resolved_url:   Service and endpoint collection :type <type, 'collections.deque'>
    """
    if not http_url:
        return deque((False, ""))

    http_url = http_url.rstrip('/')
    resolved_list = http_url.split('/', 1)
    resolved_list.insert(0, True)
    return deque(resolved_list)


def resolve_response_from_provider(http_response):
    """
    Resolves the response got from the provider into one of three possible results. The response
    can be succeeded or failed with the appropriate reason.
    If failed then an error is raised with the appropriate code.

    :param http_response:       The http response gotten from the provider as response to our
                                http request
                                :type <type, 'flask.wrappers.Response'>
    :return valid_response:     Boolean value specifying validity or invalidity of the response
                                :type <type, 'bool'>
    """
    if http_response.status_code == 200:
        return True
    else:
        return False


def resolve_token_privileges(http_request, resolved_token):
    """
    Resolves the deserialized token to ensure it has the privileges to perform the
    `action` specified at the `destination` specified.

    :param http_request:    The http request sent from the client.
                            :type <type, 'flask.wrappers.Request'>

    :param resolved_token   The authentication token as deserialized by the authentication
                            service.
                            :type <type, 'dict'>

    :return is_privy        Boolean specifying if the http_request is privileged enough to
                            perform the action and access the endpoint it is interested in.
                            :type <type, 'bool'>
    """
    pass


def validate_parameter_values(parameter_value, filters=None, **kwargs):
    """
    Validates parameter values based on the filters provided. These filters are declared in the constants
    modules and ensure that the parameter is valid to be saved. Invalid values could meant it contains
    spaces, numbers, symbols, blank space characters etc.

    var_args

    :param parameter_value:         The parameter value to perform checks on. It could be a number or string
                                    or collection.
                                    :type <type, 'object'>

    :param filters:                 A collection of invalid checks to perform on the parameter value.
                                    :type <type, 'list'>

    :param var_args:                A variable collection of arguments to use in preconditioning the expected
                                    criteria that the validation must meet. i.e. minimum length and specific error
                                    message to be displayed amongst others.
                                    dictionary keys limited to : `length`, `suffix`, `symbol`
                                    :type <type, 'dict'>

    :return valid_parameter:        A boolean value specifying if the parameter is valid or not.
                                    :type <type, 'bool'>
    """
    min_length = kwargs.get("length")
    suffix = kwargs.get("suffix", "String")  #: Use the word `String` as a suffix if suffix is empty
    symbol = kwargs.get("symbol")
    symbols = kwargs.get("symbols")
    maximum = kwargs.get("max")
    minimum = kwargs.get("minimum")

    for filter in filters:
        if filter not in FILTER_COLLECTION:
            raise AttributeError("Filter not a valid value validation filter")
        if filter == NOT_EMPTY:
            __validate_not_empty(parameter_value, suffix)
        if filter == NO_SPACE:
            __validate_no_spaces(parameter_value, suffix)
        if filter == NO_NUMBER:
            __validate_no_numbers(parameter_value, suffix)
        if filter == NO_SYMBOL:
            __validate_no_symbols(parameter_value, suffix)
        if filter == HAS_CAPS:
            __validate_has_caps(parameter_value, suffix)
        if filter == HAS_EMPTY:
            __validate_has_empty(parameter_value, suffix)
        if filter == HAS_LENGTH:
            __validate_has_length(parameter_value, suffix)
        if filter == HAS_SPACE:
            __validate_has_space(parameter_value, suffix)
        if filter == HAS_NUMBER:
            __validate_has_number(parameter_value, suffix)
        if filter == HAS_SYMBOL:
            __validate_has_symbol(parameter_value, suffix)


def __validate_has_caps(parameter, suffix):
    """
    Validates the parameter has at least a single capitalized character.

    :param parameter:           The parameter that should contains a capitalized
                                member.
                                :type <type, 'str'>

    :return has_caps:           Boolean indicating the presence or absence of caps
    """
    parameter = str(parameter)
    for alphabet in parameter:
        if alphabet.isupper():
            return True
    raise InvalidValueError(HAS_CAPS_MESSAGE_CANNED.format(suffix))


def __validate_has_empty(parameter, suffix=None):
    """
    Validates the parameter is empty by using the intrinsic truth value nature of python types.

    :param parameter:           The parameter to ensure emptiness of, this can be an
                                empty list, tuple, string or dictionary.
                                :type <type, 'Sequence'>

    :return has_empty:          Boolean indicating the emptiness value of the parameter
    """
    if not bool(parameter):  #: Using the truth valueness of python :-)
        return True
    raise InvalidValueError(HAS_EMPTY_MESSAGE_CANNED.format(suffix))


def __validate_has_number(parameter, suffix=None):
    """
    Validates the parameter has at least one number.

    :param parameter:           The parameter to validate for presence of a number
                                :type <type, 'Sequence'>

    :return has_number:         Boolean indicating presence or absence of a number
    """
    parameter = str(parameter)
    parameter.strip()
    for alphabet in parameter:
        if alphabet.isdigit():
            return True
    raise InvalidValueError(HAS_NUMBER_MESSAGE_CANNED.format(suffix))


def __validate_has_length(parameter, suffix=None, min_length=6):
    """
    Validates the parameter is longer than the specified length

    :param parameter:           The parameter to verify for length
                                :type <type, 'str'>
                                :type <type, 'list'>

    :param min_length:          The minimum length wanted
                                :type <type, 'int'>

    :return has_length:         Boolean indicating if the parameter met the minimum length
                                requirements as specificed by the :param min_length.
                                :type <type, 'Sequence'>
    """
    if len(parameter) < min_length:
        raise InvalidValueError(HAS_LENGTH_MESSAGE_CANNED.format(suffix))
    return True


def __validate_has_space(parameter, suffix=None):
    """
    Validates the parameter contains spaces.

    :param parameter:       The parameter contains spaces
    :return validity:       Boolean value or error if failed
    """
    parameter = str(parameter)
    for alphabet in parameter:
        if alphabet.isspace():
            return True
    raise InvalidValueError(HAS_SPACE_MESSAGE_CANNED.format(suffix))


def __validate_has_symbol(parameter, suffix=None, symbol=None, symbols=None):
    """
    Validates the parameter contains any symbols.

    :param parameter:       The parameter that should contain spaces
                            :type <type, 'str'>

    :param symbol:          A symbol to use as validation check i.e. parameter has
                            the symbol.
                            :type <type, 'str'>

    :return validity:       Boolean value or error if failed
    """
    for alphabet in parameter:
        if not (alphabet.isalnum() or alphabet.isspace()):
            return True
    raise InvalidValueError(HAS_SYMBOL_MESSAGE_CANNED.format(suffix))


def __validate_no_numbers(parameter, suffix=None):
    """
    Validates the parameter does not contain any numbers.

    :param parameter:           The parameter to validate for absence of numbers
                                :type <type, 'Sequence'>
    :return:
    """
    parameter = str(parameter)
    parameter.strip()
    for alphabet in parameter:
        if alphabet.isdigit():
            raise InvalidValueError(NO_NUMBER_MESSAGE_CANNED.format(suffix))
    return True


def __validate_no_spaces(parameter, suffix=None):
    """
    Validates the parameter does not contain any spaces.

    :param parameter:           The parameter contains spaces
    :return:
    """
    parameter = str(parameter)
    parameter.strip()
    for alphabet in parameter:
        if alphabet.isspace():
            raise InvalidValueError(NO_SPACE_MESSAGE_CANNED.format(suffix))
    return True


def __validate_no_symbols(parameter, suffix=None):
    """
    Validates the parameter does not contain any symbols.

    :param parameter:           The parameter contains spaces
    :return:
    """
    parameter = str(parameter)
    parameter.strip()
    for alphabet in parameter:
        if not alphabet.isalnum():
            raise InvalidValueError(NO_SYMBOL_MESSAGE_CANNED.format(suffix))
    return True


def __validate_not_empty(parameter, suffix=None):
    """
    Validates the parameter is not empty.

    :param parameter:           The parameter contains spaces
    :return:
    """
    length = len(parameter)
    if length == 0:
        raise InvalidValueError(NOT_EMPTY_MESSAGE_CANNED.format(suffix))
    return True
