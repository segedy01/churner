"""
Test the code constants do not change arbitarily as certain tests may
depend on them
"""

from application.constants.codes.error import *

ACCOUNT_NOT_FOUND_CODE_TEST = 10911

BAD_TOKEN_CODE_TEST = 12204

CREDENTIAL_NOT_FOUND_CODE_TEST = 10908
DUPLICATE_USER_CODE_TEST = 10902
DUPLICATE_RESOURCE_CODE_TEST = 10906

EXPIRED_TOKEN_CODE_TEST = 10100

INTERNAL_SERVER_ERROR_CODE_TEST = 10900

INVALID_CREDENTIALS_CODE_TEST = 10101
INVALID_HEADER_CODE_TEST = 12200
INVALID_PARAMETERS_CODE_TEST = 12203
INVALID_REQUEST_CODE_TEST = 12207
INVALID_RESPONSE_CODE_TEST = 10904
INVALID_TOKEN_CODE_TEST = 10103
INVALID_URL_CODE_TEST = 12206
INVALID_VALUE_CODE_TEST = 12208


MISMATCHED_PARAMETERS_CODE_TEST = 12205
MISSING_HEADER_CODE_TEST = 12201
MISSING_PARAMETER_CODE_TEST = 12202
MISSING_RESOURCE_CODE_TEST = 12209

PASSWORD_MISMATCH_CODE_TEST = 12211
PROVIDER_NOT_FOUND_CODE_TEST = 10905


SERVICE_UNAVAILABLE_CODE_TEST = 10901
SERVICE_NOT_FOUND_CODE_TEST = 10903

USER_NOT_FOUND_CODE_TEST = 10906

WRONG_CREDENTIAL_CODE_TEST = 10104
WRONG_PARAMETER_CODE_TEST = 10105

VALIDATION_FAILED_CODE_TEST = 12210

def test_error_codes():
    assert ACCOUNT_NOT_FOUND_CODE_TEST == ACCOUNT_NOT_FOUND_CODE
    assert BAD_TOKEN_CODE_TEST == BAD_TOKEN_CODE
    assert CREDENTIAL_NOT_FOUND_CODE_TEST == CREDENTIAL_NOT_FOUND_CODE
    assert DUPLICATE_USER_CODE_TEST == DUPLICATE_USER_CODE
    assert DUPLICATE_RESOURCE_CODE_TEST == DUPLICATE_RESOURCE_CODE
    assert EXPIRED_TOKEN_CODE_TEST == EXPIRED_TOKEN_CODE
    assert INTERNAL_SERVER_ERROR_CODE_TEST == INTERNAL_SERVER_ERROR_CODE
    assert INVALID_CREDENTIALS_CODE_TEST == INVALID_CREDENTIALS_CODE
    assert INVALID_HEADER_CODE_TEST == INVALID_HEADER_CODE
    assert INVALID_PARAMETERS_CODE_TEST == INVALID_PARAMETERS_CODE
    assert INVALID_REQUEST_CODE_TEST == INVALID_REQUEST_CODE
    assert INVALID_RESPONSE_CODE_TEST == INVALID_RESPONSE_CODE
    assert INVALID_TOKEN_CODE_TEST == INVALID_TOKEN_CODE
    assert INVALID_URL_CODE_TEST == INVALID_URL_CODE
    assert INVALID_VALUE_CODE_TEST == INVALID_VALUE_CODE
    assert MISMATCHED_PARAMETERS_CODE_TEST == MISMATCHED_PARAMETERS_CODE
    assert MISSING_HEADER_CODE_TEST == MISSING_HEADER_CODE
    assert MISSING_PARAMETER_CODE_TEST == MISSING_PARAMETER_CODE
    assert MISSING_RESOURCE_CODE_TEST == MISSING_RESOURCE_CODE
    assert PASSWORD_MISMATCH_CODE_TEST == PASSWORD_MISMATCH_CODE
    assert PROVIDER_NOT_FOUND_CODE_TEST == PROVIDER_NOT_FOUND_CODE
    assert SERVICE_UNAVAILABLE_CODE_TEST == SERVICE_UNAVAILABLE_CODE
    assert SERVICE_NOT_FOUND_CODE_TEST == SERVICE_NOT_FOUND_CODE
    assert USER_NOT_FOUND_CODE_TEST == USER_NOT_FOUND_CODE
    assert WRONG_CREDENTIAL_CODE_TEST == WRONG_CREDENTIAL_CODE
    assert WRONG_PARAMETER_CODE_TEST == WRONG_PARAMETER_CODE
    assert VALIDATION_FAILED_CODE_TEST == VALIDATION_FAILED_CODE
