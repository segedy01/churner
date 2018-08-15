"""
Auto generates Fetch Standard Json Formatted response dictionaries for further jsonification by flask Jsonify

application.modules.api.rest.autojsonify
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Collection of wrapper functions to generate different scenarios of json formatted dictionaries or collections
"""

from collections import OrderedDict

from flask import jsonify

from application.constants import (HTTP_UNAUTHORIZED, HTTP_NOT_FOUND, HTTP_CONFLICT)
from application.modules.core.exc.failed import DuplicateUserError, PasswordMismatchError
from application.modules.core.exc.missing import (
    MissingHeaderException, CredentialNotFoundError, UserNotFoundError, MissingResourceError
)
from application.modules.core.exc.invalid import InvalidCredentialsError

def _is_any_instance(obj, *args):
    for i in args:
        if isinstance(obj, i):
            return True
    return False

def json_failure(exception, status_code=None, error_code=None):
    if not status_code:
        if isinstance(exception, PasswordMismatchError):
            status_code = 422
        elif _is_any_instance(exception, CredentialNotFoundError, 
            InvalidCredentialsError):
            status_code = HTTP_UNAUTHORIZED
        elif _is_any_instance(exception, UserNotFoundError, MissingResourceError):
            status_code = HTTP_NOT_FOUND
        elif _is_any_instance(exception, DuplicateUserError):
            status_code = HTTP_CONFLICT
        else:
            status_code = 500

    message = None
    code = None
    try:
        message = exception.message
        if error_code:
            code = error_code
        else:
            code = exception.code
    except:
        pass

    json_payload = {}
    if message == None and code == None:
        json_payload['success'] = False
        json_payload['message'] = "internal server error"
        json_payload['code'] = 0
    else:
        json_payload = generate_failed_json(message, code)
        del json_payload['status']
        json_payload['success'] = False
        json_payload['code'] = json_payload['error'] if not code else code
        del json_payload['error']

    return jsonify(json_payload), status_code

def auto_generate_failed_json(exception_instance):
    """
    Auto generates failed json messsage from an exception instance. Functionally similar to
    the :method `generate_failed_json` and uses this method to generate json by passing in the code
    and message resolved from the exception instance.

    :param exception_instance:      Custom exception instance that contains a code and message pertaining
                                    to the failure.
    :return:
    """
    return generate_failed_json(exception_instance.message, exception_instance.code)


def resolve_json_data_payload(value):
    """
    Checks the type of value corresponds to a dict or is None and returns the value that matches either

    :param value:
    :return:
    """
    if isinstance(value, dict):
        return [value]
    elif isinstance(value, list):
        return value
    elif value is None:
        return
    else:
        raise ValueError('Invalid data payload type, payload type must be json resolvable')


def generate_denied_message(message, error_code):
    """
    Generates an authorized response message

    This message is generated in response to an unauthorized request to the protected resources
    sitting behind the Fetchr protected resources great wall of china, well not exactly a great wall
    but more of a very lovely looking picket fence

    :param message:     The message to return as reason to the client for instruction
                        :type <type, 'str'>

    :param error_code:  The fetchr internal error code used by fetchr to identify and track common
                        known and uncommon unknown errors and or exceptions
                        :type <type, 'str'>

    :return:            The collection object that holds the formatted key value collections
                        :type <type, 'dict'>
    """
    denied_json = generate_failed_json(message, error_code)
    return denied_json


def generate_failed_json(message, error_code):
    """
    Generates a failure response json message

    :param message:     The message to return as reason for failure
                        :type <type, 'str'>
    :param error_code:  The fetchr internal error code used by fetchr to identify and track common
                        known and uncommon unknown errors and or exceptions
                        :type <type, 'str'>
    :return:            The collection object that holds the formatted key value collections
                        :type <type, 'dict'>
    """
    failed_json_object = OrderedDict()

    failed_json_object['status'] = 'failed'
    failed_json_object['message'] = message
    failed_json_object['error'] = error_code

    return failed_json_object


def generate_success_message(data):
    """
    Generates successful operation json message from the valid json resolvable :param `data`

    This :param `data` is what ends up as the value of the data key of all successful json responses
    this in line with the json schema chosen to represent all fetchr json responses
    :see http:\\www.jsonapi.com/schema for more information.

    :param data:            The data to be appended as the value of the json response key of the same
                            name i.e. `data`
                            :type <type, 'object'> limited to [str, int, list, None]
    :return success_json:   The fully parsed json response dict, might require additional wrapping by flask
                            json generating header function
                            :type <type, 'collections.OrderedDict'>
    """
    resolved_data = resolve_json_data_payload(data)
    success_json = OrderedDict()

    success_json['status'] = 'success'
    success_json['data'] = resolved_data
    return success_json
