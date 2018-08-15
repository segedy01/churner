"""
Repository for all the constants to be used in the application
"""
from collections import OrderedDict

from .codes.error import *
from .codes.http import *
from .messages.error import *
from .messages.http import *

from application.modules.core.wrappers import LookupDict

ALL_TOKEN_TTL = 60 * 15 #: 15mins

AUTH_REGEX = r'^(?!.*(,)).*Bearer\s[a-zA-Z0-9]+:[a-zA-Z0-9]+'
AUTH_STRING_REGEX = r'^(?!.*(,)).*Bearer\s[a-zA-Z0-9]+'
AUTHENTICATION_TYPE = 'Bearer'

ENSURE_VERIFY_PASSWORD = True
ENSURE_EMAIL_UNIQUE = False

HAS_CAPS = 10
HAS_EMPTY = 11
HAS_LENGTH = 12
HAS_SPACE = 13
HAS_SYMBOL = 14
HAS_NUMBER = 15

NO_NUMBER = 0
NO_SPACE = 1
NO_SYMBOL = 2
NOT_EMPTY = 3
FILTER_COLLECTION = [
    HAS_CAPS,
    HAS_EMPTY,
    HAS_LENGTH,
    HAS_NUMBER,
    HAS_SPACE,
    HAS_SYMBOL,
    NO_NUMBER,
    NO_SPACE,
    NO_SYMBOL,
    NOT_EMPTY
]
REDIS_AUTH_TOKEN_PREFIX = 'credential:'
SERVICES = [
    "awb",
    "couriers",
    "orders",
    "tracking",
]


############################
#: AUTHENTICATION ERRORS 101
expired_token = LookupDict(code=EXPIRED_TOKEN_CODE, message=EXPIRED_TOKEN_MESSAGE)
invalid_credentials = LookupDict(code=INVALID_CREDENTIALS_CODE, message=INVALID_CREDENTIALS_MESSAGE)
invalid_token = LookupDict(code=INVALID_TOKEN_CODE, message=INVALID_TOKEN_MESSAGE)
wrong_credentials = LookupDict(code=WRONG_CREDENTIAL_CODE, message=WRONG_CREDENTIALS_MESSAGE)
password_mismatch = LookupDict(code=PASSWORD_MISMATCH_CODE, message=PASSWORD_MISMATCH_MESSAGE)
incorrect_password_error = LookupDict(code=PASSWORD_INCORRECT_CODE, message=PASSWORD_INCORRECT_MESSAGE)
credential_not_found = LookupDict(code=CREDENTIAL_NOT_FOUND_CODE, message=CREDENTIAL_NOT_FOUND_MESSAGE)

#: Container
authentication_errors = {
    "invalid_credentials": invalid_credentials,
    "expired_token": expired_token,
    "invalid_token": invalid_token,
    "password_mismatch": password_mismatch,
    "incorrect_password_error": incorrect_password_error,
    "wrong_credentials": wrong_credentials,
    "credential_not_found": credential_not_found
}


########################
#: VALIDATION ERRORS 122
validation_failed = LookupDict(code=VALIDATION_FAILED_CODE, message=VALIDATION_FAILED_MESSAGE)
invalid_header = LookupDict(code=INVALID_HEADER_CODE, message=INVALID_HEADER_MESSAGE)
missing_header = LookupDict(code=MISSING_HEADER_CODE, message=MISSING_HEADER_MESSAGE)
missing_parameter = LookupDict(code=MISSING_PARAMETER_CODE, message=MISSING_PARAMETER_MESSAGE)
wrong_parameter = LookupDict(code=WRONG_PARAMETER_CODE, message=WRONG_PARAMETER_MESSAGE)
bad_token = LookupDict(code=BAD_TOKEN_CODE, message=BAD_TOKEN_MESSAGE)
mismatched_parameters = LookupDict(code=MISMATCHED_PARAMETERS_CODE, message=MISMATCHED_PARAMETERS_MESSAGE)
invalid_url = LookupDict(code=INVALID_URL_CODE, message=INVALID_URL_MESSAGE)
invalid_request = LookupDict(code=INVALID_REQUEST_CODE, message=BAD_REQUEST_MESSAGE)
invalid_parameters = LookupDict(code=INVALID_PARAMETERS_CODE, message=INVALID_PARAMETERS_MESSAGE)
invalid_value = LookupDict(code=INVALID_VALUE_CODE, message=INVALID_VALUE_MESSAGE)
missing_resource = LookupDict(code=MISSING_RESOURCE_CODE, message=MISSING_RESOURCE_MESSAGE)
invalid_credentials = LookupDict(code=INVALID_CREDENTIALS_CODE, message=INVALID_CREDENTIALS_MESSAGE)
invalid_response = LookupDict(code=INVALID_RESPONSE_CODE, message=INVALID_RESPONSE_MESSAGE)


#: Container
validation_errors = {
    "missing_parameter": missing_parameter,
    "invalid_header": invalid_header,
    "missing_header": missing_header,
    "wrong_parameter": wrong_parameter,
    "bad_token": bad_token,
    "mismatched_parameters": mismatched_parameters,
    "invalid_url": invalid_url,
    "invalid_request": invalid_request,
    "validation_failed": validation_failed,
    "invalid_parameters": invalid_parameters,
    "invalid_value": invalid_value,
    "missing_resource": missing_resource,
    "invalid_credentials": invalid_credentials,
    "invalid_response": invalid_response
}


########################
#: INTERNAL ERRORS 109
internal_server_error = LookupDict(code=INTERNAL_SERVER_ERROR_CODE, message=SERVER_ERROR_MESSAGE)
service_unavailable = LookupDict(code=SERVICE_UNAVAILABLE_CODE, message=SERVICE_UNAVAILABLE_MESSAGE)
duplicate_user = LookupDict(code=DUPLICATE_USER_CODE, message=DUPLICATE_USER_MESSAGE)
duplicate_resource = LookupDict(code=DUPLICATE_RESOURCE_CODE, message=DUPLICATE_RESOURCE_MESSAGE)
service_not_found_error = LookupDict(code=SERVICE_NOT_FOUND_CODE, message=SERVICE_NOT_FOUND_MESSAGE)
no_response = LookupDict(code=INVALID_RESPONSE_CODE, message=INVALID_RESPONSE_MESSAGE)
provider_not_found = LookupDict(code=PROVIDER_NOT_FOUND_CODE, message=PROVIDER_NOT_FOUND_MESSAGE)
user_not_found = LookupDict(code=USER_NOT_FOUND_CODE, message=USER_NOT_FOUND_MESSAGE)
account_not_found = LookupDict(code=ACCOUNT_NOT_FOUND_CODE, message=ACCOUNT_NOT_FOUND_MESSAGE)
file_not_found = LookupDict(code=FILE_NOT_FOUND_CODE, message=FILE_NOT_FOUND_MESSAGE)

#: Container
internal_errors = {
    "service_unavailable": service_unavailable,
    "duplicate_user": duplicate_user,
    "duplicate_resource": duplicate_resource,
    "internal_server": internal_server_error,
    "service_not_found": service_not_found_error,
    "no_response": no_response,
    "provider_not_found": provider_not_found,
    "user_not_found": user_not_found,
    "account_not_found": account_not_found,
    "file_not_found": file_not_found
}


#: Create an ERROR_CODES container collection to hold all the error objects
ERROR_CODES = OrderedDict()

#: Instantiate the error objects unto the ERROR_CODES container collections
ERROR_CODES.authentication_errors = authentication_errors
ERROR_CODES.validation_errors = validation_errors
ERROR_CODES.internal_errors = internal_errors
