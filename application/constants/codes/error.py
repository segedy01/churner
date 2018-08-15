"""
Holds error codes to help identify problems
"""
ACCOUNT_NOT_FOUND_CODE = 10911

BAD_TOKEN_CODE = 12204

CREDENTIAL_NOT_FOUND_CODE = 10908
DUPLICATE_USER_CODE = 10902
REVERIFY_USER_CODE = 10999  #use this code to indicate that a user already exists 
#and needs reverification
DUPLICATE_RESOURCE_CODE = 10906

EXPIRED_TOKEN_CODE = 10100

INTERNAL_SERVER_ERROR_CODE = 10900

INVALID_CREDENTIALS_CODE = 10101
INVALID_HEADER_CODE = 12200
INVALID_PARAMETERS_CODE = 12203
INVALID_REQUEST_CODE = 12207
INVALID_RESPONSE_CODE = 10904
INVALID_TOKEN_CODE = 10103
INVALID_URL_CODE = 12206
INVALID_VALUE_CODE = 12208


MISMATCHED_PARAMETERS_CODE = 12205
MISSING_HEADER_CODE = 12201
MISSING_PARAMETER_CODE = 12202
MISSING_RESOURCE_CODE = 12209

PASSWORD_MISMATCH_CODE = 12211
PASSWORD_INCORRECT_CODE = 12212
PROVIDER_NOT_FOUND_CODE = 10905


SERVICE_UNAVAILABLE_CODE = 10901
SERVICE_NOT_FOUND_CODE = 10903

USER_NOT_FOUND_CODE = 10906

WRONG_CREDENTIAL_CODE = 10104
WRONG_PARAMETER_CODE = 10105

VALIDATION_FAILED_CODE = 12210

FILE_NOT_FOUND_CODE = 100440


__all__ = [
    'ACCOUNT_NOT_FOUND_CODE',
    'BAD_TOKEN_CODE',
    'CREDENTIAL_NOT_FOUND_CODE',
    'DUPLICATE_USER_CODE',
    'DUPLICATE_RESOURCE_CODE',
    'EXPIRED_TOKEN_CODE',
    'INTERNAL_SERVER_ERROR_CODE',
    'INVALID_CREDENTIALS_CODE',
    'INVALID_HEADER_CODE',
    'INVALID_PARAMETERS_CODE',
    'INVALID_REQUEST_CODE',
    'INVALID_RESPONSE_CODE',
    'INVALID_TOKEN_CODE',
    'INVALID_URL_CODE',
    'INVALID_VALUE_CODE',
    'MISMATCHED_PARAMETERS_CODE',
    'MISSING_HEADER_CODE',
    'MISSING_PARAMETER_CODE',
    'MISSING_RESOURCE_CODE',
    'PASSWORD_MISMATCH_CODE',
    'PASSWORD_INCORRECT_CODE',
    'PROVIDER_NOT_FOUND_CODE',
    'SERVICE_NOT_FOUND_CODE',
    'SERVICE_UNAVAILABLE_CODE',
    'USER_NOT_FOUND_CODE',
    'WRONG_CREDENTIAL_CODE',
    'WRONG_PARAMETER_CODE',
    'VALIDATION_FAILED_CODE',
    'FILE_NOT_FOUND_CODE'
]
