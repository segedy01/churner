"""
Errors that have to do with failures live here. Both internal and external

application.modules.core.exc.failed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from application.constants import ERROR_CODES


class DuplicateUserError(Exception):
    """
    Custom error to raise when a user that already exists on the system is trying to be
    overriden in a post request.
    """

    def __init__(self, *args, **kwargs):

        duplicate_user_error = ERROR_CODES.internal_errors.get('duplicate_user')

        self.message = duplicate_user_error.message
        self.code = duplicate_user_error.code

        if len(args) > 0:
            self.message = args[0]

        super(DuplicateUserError, self).__init__(self.message)


class DuplicateResourceError(Exception):
    """
    Custom error to raise when another resource that already exists on the system is trying to be
    overriden in a post request. Can be used in place of a duplicate user error but not vis a vis.
    """

    def __init__(self, *args, **kwargs):
        duplicate_resource_error = ERROR_CODES.internal_errors.get('duplicate_resource')
        self.code = duplicate_resource_error.code
        self.message = duplicate_resource_error.message

        if len(args) > 0:
            self.message = args[0]

        super(DuplicateResourceError, self).__init__(self.message)


class InternalServerError(Exception):
    """
    Custom exception to raise when an Error occurs in internal systems due to
    some unforeseen circumstance

    application.modules.core.exc.failed.InternalServerError
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    """

    def __init__(self, *args, **kwargs):
        internal_server_error = ERROR_CODES.internal_errors.get('internal_server')
        self.code = internal_server_error.code
        self.message = internal_server_error.message

        if len(args) > 0:
            self.message = args[0]

        super(InternalServerError, self).__init__(self.message)

class ImproperlyConfiguredError(InternalServerError):
    """
    Custom exception to raise when an the server is improperly configured

    application.modules.core.exc.failed.InternalServerError
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    """
    pass


class PasswordMismatchError(Exception):
    """
    Custom extension of exception to provide representation for scenarios where the verify
    password field did not match the primary password field.

    application.modules.core.exc.invalid.PasswordMismatchError
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

    def __init__(self, *args, **kwargs):

        password_mismatch_error = ERROR_CODES.authentication_errors.get('password_mismatch')
        self.code = password_mismatch_error.code
        self.message = password_mismatch_error.message
        if len(args) > 0:
            self.message = args[0]

        super(PasswordMismatchError, self).__init__(self.message)


class IncorrectPasswordError(Exception):
    """
    Custom extension of exception to provide representation for scenarios where
    the password input is not correct

    application.modules.core.exc.invalid.IncorrectPasswordError
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

    def __init__(self, *args, **kwargs):

        incorrect_password_error = ERROR_CODES.authentication_errors.get('incorrect_password_error')
        self.code = incorrect_password_error.code
        self.message = incorrect_password_error.message
        if len(args) > 0:
            self.message = args[0]

        super(IncorrectPasswordError, self).__init__(self.message)


class ServiceNotFoundError(Exception):
    """
    Service not found error occurs when the service ip address could not be gotten
    from the service registry due to a bad service name.

    application.modules.core.exc.failed.ServiceUnavailableError
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

    def __init__(self, *args, **kwargs):
        service_unavailable_error = ERROR_CODES.internal_errors.get('service_not_found')
        self.code = service_unavailable_error.code
        self.message = service_unavailable_error.message

        if len(args) > 0:
            self.message = args[0]

        super(ServiceNotFoundError, self).__init__(self.message)


class ServiceUnavailableError(Exception):
    """
    Service unavailable error occurs when the service is valid but is unhealthy.

    application.modules.core.exc.failed.ServiceUnavailableError
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

    def __init__(self, *args, **kwargs):
        service_unavailable_error = ERROR_CODES.internal_errors.get('service_unavailable')
        self.code = service_unavailable_error.code
        self.message = service_unavailable_error.message

        if len(args) > 0:
            self.message = args[0]

        super(ServiceUnavailableError, self).__init__(self.message)

class ExpiredError(Exception):
    def __init__(self, *args, **kwargs):
        expired_error = ERROR_CODES.authentication_errors.get('expired_token')
        self.code = expired_error.code
        self.message = expired_error.message

        if len(args) > 0:
            self.message = args[0]

        super(ExpiredError, self).__init__(self.message)


class ConfirmationTimeError(Exception):
    """
    Confirmation error occurs when Deserialisation. raised when token confirmaton fails 
    due to expired time
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
    """

    def __init__(self, *args, **kwargs):
        confirmation_time_error = ERROR_CODES.authentication_errors.get('expired_token')
        self.code = confirmation_time_error.code
        self.message = confirmation_time_error.message

        if len(args) > 0:
            self.message = args[0]

        super(ConfirmationTimeError, self).__init__(self.message)

class FileNotFound(Exception):

    def __init__(self, *args, **kwargs):
        file_not_found_error = ERROR_CODES.internal_errors.get('file_not_found')
        self.code = file_not_found_error.code
        self.message = file_not_found_error.message

        if len(args) > 0:
            self.message = args[0]

        super(FileNotFound, self).__init__(self.message)

