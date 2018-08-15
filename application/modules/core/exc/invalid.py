"""
Custom exceptions that arise from invalid resources or artefacts live here

application.modules.core.exc.invalid
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from application.constants import ERROR_CODES


class InvalidCredentialsError(Exception):
    """
    Custom extension of exception to provide representation
    for scenarios where an invalid parameter type is used in a
    context it was not expected or supported.

    application.modules.core.exc.invalid.InvalidParametersError
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

    def __init__(self, *args, **kwargs):

        invalid_credentials_error = \
            ERROR_CODES.authentication_errors.get('invalid_credentials')
        self.code = invalid_credentials_error.code
        self.message = invalid_credentials_error.message
        if len(args) > 0:
            self.message = args[0]

        super(InvalidCredentialsError, self).__init__(self.message)


class InvalidHeaderError(Exception):
    """
    Header exception is an exception raised as a
    result of improperly formatted header values
    """

    def __init__(self, *args, **kwargs):
        invalid_header_error = \
            ERROR_CODES.validation_errors.get('invalid_header')

        self.message = invalid_header_error.message
        self.code = invalid_header_error.code

        if len(args) > 0:
            self.message = args[0]

        super(InvalidHeaderError, self).__init__(self.message)


class InvalidParametersError(Exception):
    """
    Custom extension of exception to provide
    representation for scenarios where an
    invalid parameter type is used in a context
    it was not expected or supported.

    application.modules.core.exc.invalid.InvalidParametersError
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

    def __init__(self, *args, **kwargs):

        invalid_parameters_error = \
            ERROR_CODES.validation_errors.get('invalid_parameters')
        self.code = invalid_parameters_error.code
        self.message = invalid_parameters_error.message
        if len(args) > 0:
            self.message = args[0]

        super(InvalidParametersError, self).__init__(self.message)


class InvalidResponseError(Exception):
    """
    Custom extension of exception to provide
    representation for scenarios where an
    invalid response type is used in a context
    it was not expected or supported.

    application.modules.core.exc.invalid.InvalidResponseError
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

    def __init__(self, *args, **kwargs):

        invalid_response_error = ERROR_CODES.internal_errors.get('no_response')
        self.code = invalid_response_error.code
        self.message = invalid_response_error.message

        if len(args) > 0:
            self.message = args[0]

        super(InvalidResponseError, self).__init__(self.message)


class InvalidUrlError(Exception):
    """
    Custom extension of exception to provide
    representation for scenarios where an
    invalid url type is used in a context
    it was not expected or supported.

    application.modules.core.exc.invalid.InvalidUrlError
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

    def __init__(self, *args, **kwargs):

        invalid_url_error = ERROR_CODES.validation_errors.get('invalid_url')
        self.code = invalid_url_error.code
        self.message = invalid_url_error.message

        if len(args) > 0:
            self.message = args[0]

        super(InvalidUrlError, self).__init__(self.message)


class InvalidRequestError(Exception):
    """
    Header exception is an exception raised as a
    result of improperly formatted header values
    """

    def __init__(self, *args, **kwargs):
        invalid_request_error = \
            ERROR_CODES.validation_errors.get('invalid_request')

        self.message = invalid_request_error.message
        self.code = invalid_request_error.code

        if len(args) > 0:
            self.message = args[0]

        super(InvalidRequestError, self).__init__(self.message)


class InvalidValueError(Exception):
    """
    Custom extension of exception to provide
    representation for scenarios where an
    invalid parameter type is used in a context
    it was not expected or supported.

    application.modules.core.exc.invalid.InvalidValueError
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

    def __init__(self, *args, **kwargs):

        invalid_value_error = \
            ERROR_CODES.validation_errors.get('invalid_value')
        self.code = invalid_value_error.code
        self.message = invalid_value_error.message

        if len(args) > 0:
            self.message = args[0]

        super(InvalidValueError, self).__init__(self.message)

class InvalidPageSizeError(InvalidValueError):
    """
    Raised when a paginator is configured with an invalid page size
    """
    pass

class InvalidPageError(InvalidValueError):
    """
    Raise when an invalid page is requested from a paginator
    """
    pass

class InvalidDateRange(InvalidValueError):
    """
    Raised when an invalid start and end date or any other date range being 
    specified is not allowed.
    """
    pass

class InvalidSalaryRange(InvalidValueError):
    """
    Raised when an invalid start and end date or any other date range being 
    specified is not allowed.
    """
    pass

class NotAuthorizedError(InvalidCredentialsError):
    """
    Raised when an entity is not autorized to make the request being processed
    """
    pass

class InvalidChannelError(InvalidValueError):
    """
    Raised if a messaging channel selected is invalid.
    """
    pass