"""
Messages constants hold messages that are used in more than one place
to provide a single point of change

application.constants.messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Candidate for refactoring: move all constant messages here or export __all__
"""
ACCOUNT_NOT_FOUND_MESSAGE = "Account matching provided details could not be found"
FILE_NOT_FOUND_MESSAGE = "File could not be located"

BAD_CREDENTIALS_MESSAGE = "The credentials provided are invalid"
BAD_JSON_MESSAGE = "The JSON body sent is malformed"
BAD_TOKEN_MESSAGE = 'Bad token used in authentication scheme'
BAD_REQUEST_MESSAGE = 'That request is so bad it made us cry'

CREDENTIAL_NOT_FOUND_MESSAGE = 'How did you get this token? From Fetchr or by Magic'

DUPLICATE_USER_MESSAGE = 'User Resource with same ID found in the system'
DUPLICATE_RESOURCE_MESSAGE = 'Another Resource with same details found in the system'

EXPIRED_TOKEN_MESSAGE = 'Your authentication token has expired'

HAS_CAPS_MESSAGE_CANNED = '{} must include CAPS'
HAS_LENGTH_MESSAGE_CANNED = '{} must be longer than 8 characters'
HAS_NUMBER_MESSAGE_CANNED = '{} must contain a number'
HAS_SPACE_MESSAGE_CANNED = '{} must contain at least an empty space'
HAS_SYMBOL_MESSAGE_CANNED = '{} must contain at least one symbol'
HAS_EMPTY_MESSAGE_CANNED = '{} not empty, must be empty'

INSUFFICIENT_PRIVILEGE_MESSAGE = "You do not have enough permissions for this action"
INVALID_CREDENTIALS_MESSAGE = 'Invalid credentials detected'
INVALID_HEADER_MESSAGE = 'Invalid header field found in request'
INVALID_PARAMETERS_MESSAGE = 'The parameter or keys passed with the request are not valid'
INVALID_RESPONSE_MESSAGE = 'We just fired someone for trying to send you bad response'
INVALID_TOKEN_MESSAGE = 'Invalid token detected'
INVALID_URL_MESSAGE = 'We tried really hard but that url not be resolved internally'
INVALID_USER_MESSAGE = 'The user information is not valid'
INVALID_JSON_VALUES_MESSAGE = 'The JSON body is missing a few important parts'
INVALID_VALUE_MESSAGE = 'The value you provided is not valid type'
INVALID_VALUE_CANNED_MESSAGE = 'The value for {} provided is not a valid type'
INTERNAL_SERVER_ERROR_MESSAGE = 'Aliens abducted our server, Superman is helping us get it back'

MISMATCHED_PARAMETERS_MESSAGE = 'Too many or too few parameters detected'
MISSING_HEADER_MESSAGE = 'You want us to answer you with no headers? tsk tsk tsk'
MISSING_HEADER_CANNED_MESSAGE = "Required header '{}' header is missing"
MISSING_PARAMETER_MESSAGE = "A required parameter is missing"
MISSING_PARAMETER_CANNED_MESSAGE = "{} is a required parameter"
MISSING_RESOURCE_MESSAGE = 'The resource you are looking for might have moved'

NO_NUMBER_MESSAGE_CANNED = "{} contains numbers, numbers not allowed"
NO_SPACE_MESSAGE_CANNED = "{} contains space, spaces not allowed"
NO_SYMBOL_MESSAGE_CANNED = "{} contains symbol, symbols not allowed"
NOT_EMPTY_MESSAGE_CANNED = "{} is empty, required fields can not be empty"

NO_JSON_FOUND_MESSAGE = "Why are you sending empty json requests?"
NO_MICROSERVICE_MESSAGE = "Backend service unavailable"
NO_MICROSERVICE_CANNED_MESSAGE = "{} microservice is unavailable"

ONLY_JSON_MESSAGE = "Your request does not know json kung fu"
ONLY_GET_MESSAGE = "Only GET methods allowed for this resource"
ONLY_POST_MESSAGE = "Only POST methods allowed for this resource"
ONLY_PUT_MESSAGE = "Only PUT methods allowed for this resource"

PASSWORD_MISMATCH_MESSAGE = "Passwords do not match each other"
PASSWORD_INCORRECT_MESSAGE = "Incorrect Password"
PROVIDER_NOT_FOUND_MESSAGE = "Provider matching provided details could not be found"

SERVER_ERROR_MESSAGE = "Aliens abducted our server, Superman is helping us get it back"
SERVER_ERROR_ALTERNATE_MESSAGE = "Sorry! A network pipe is broken. Try again later"
SERVICE_UNAVAILABLE_MESSAGE = 'Service currently unavailable. Try again later'
SERVICE_NOT_FOUND_MESSAGE = 'Are you sure we provide this functionality'

USELESS_JSON_FOUND_MESSAGE = "How do we say this, your JSON is useless, add appropriate keys"
USER_NOT_FOUND_MESSAGE = "User account does not exist"
UNAUTHORIZED_MESSAGE = "You do not have sufficient privileges to perform this action"

VALIDATION_FAILED_MESSAGE = "Oops your request failed to validate, correct and try again"

WRONG_CREDENTIALS_MESSAGE = "These credentials could not be tied to a user account"
WRONG_PARAMETER_MESSAGE = 'Provided the wrong type for a required parameter'

__all__ = [
    'ACCOUNT_NOT_FOUND_MESSAGE',
    'BAD_CREDENTIALS_MESSAGE',
    'BAD_JSON_MESSAGE',
    'BAD_TOKEN_MESSAGE',
    'BAD_REQUEST_MESSAGE',
    'CREDENTIAL_NOT_FOUND_MESSAGE',
    'DUPLICATE_USER_MESSAGE',
    'DUPLICATE_RESOURCE_MESSAGE',
    'EXPIRED_TOKEN_MESSAGE',
    'HAS_CAPS_MESSAGE_CANNED',
    'HAS_EMPTY_MESSAGE_CANNED',
    'HAS_LENGTH_MESSAGE_CANNED',
    'HAS_NUMBER_MESSAGE_CANNED',
    'HAS_SPACE_MESSAGE_CANNED',
    'HAS_SYMBOL_MESSAGE_CANNED',
    'INSUFFICIENT_PRIVILEGE_MESSAGE',
    'INVALID_CREDENTIALS_MESSAGE',
    'INVALID_HEADER_MESSAGE',
    'INVALID_JSON_VALUES_MESSAGE',
    'INVALID_PARAMETERS_MESSAGE',
    'INVALID_RESPONSE_MESSAGE',
    'INVALID_TOKEN_MESSAGE',
    'INVALID_URL_MESSAGE',
    'INVALID_VALUE_MESSAGE',
    'INVALID_VALUE_CANNED_MESSAGE',
    'INTERNAL_SERVER_ERROR_MESSAGE',
    'MISMATCHED_PARAMETERS_MESSAGE',
    'MISSING_HEADER_MESSAGE',
    'MISSING_HEADER_CANNED_MESSAGE',
    'MISSING_PARAMETER_MESSAGE',
    'MISSING_PARAMETER_CANNED_MESSAGE',
    'MISSING_RESOURCE_MESSAGE',
    'NOT_EMPTY_MESSAGE_CANNED',
    'NO_NUMBER_MESSAGE_CANNED',
    'NO_SPACE_MESSAGE_CANNED',
    'NO_SYMBOL_MESSAGE_CANNED',
    'NO_JSON_FOUND_MESSAGE',
    'NO_MICROSERVICE_MESSAGE',
    'NO_MICROSERVICE_CANNED_MESSAGE',
    'ONLY_GET_MESSAGE',
    'ONLY_JSON_MESSAGE',
    'ONLY_POST_MESSAGE',
    'ONLY_PUT_MESSAGE',
    'PASSWORD_MISMATCH_MESSAGE',
    'PASSWORD_INCORRECT_MESSAGE',
    'PROVIDER_NOT_FOUND_MESSAGE',
    'SERVER_ERROR_MESSAGE',
    'SERVER_ERROR_ALTERNATE_MESSAGE',
    'SERVICE_UNAVAILABLE_MESSAGE',
    'SERVICE_NOT_FOUND_MESSAGE',
    'UNAUTHORIZED_MESSAGE',
    'USELESS_JSON_FOUND_MESSAGE',
    'USER_NOT_FOUND_MESSAGE',
    'VALIDATION_FAILED_MESSAGE',
    'WRONG_CREDENTIALS_MESSAGE',
    'WRONG_PARAMETER_MESSAGE',
    'FILE_NOT_FOUND_MESSAGE'
]
