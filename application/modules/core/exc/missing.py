"""
Missing resources exceptions live here

application.modules.core.exc.missing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from application.constants import ERROR_CODES


class AccountNotFoundError(Exception):
    """
    Account not found error is raised when an invalid account id is provided to the system as input
    for account lookup

    application.modules.core.exc.missing.AccountNotFoundError
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

    def __init__(self, *args, **kwargs):
        account_not_found = ERROR_CODES.internal_errors.get('account_not_found')

        self.message = account_not_found.message
        self.code = account_not_found.code

        if len(args) > 0:
            self.message = args[0]

        super(AccountNotFoundError, self).__init__(self.message)


class CredentialNotFoundError(Exception):
    """
    Provider not found error is raised when an invalid provider id is provided to the system
    as input for provider lookup.

    application.modules.core.exc.missing.ProviderNotFoundError
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

    def __init__(self, *args, **kwargs):
        credential_not_found = ERROR_CODES.authentication_errors.get('credential_not_found')

        self.message = credential_not_found.message
        self.code = credential_not_found.code

        if len(args) > 0:
            self.message = args[0]

        super(CredentialNotFoundError, self).__init__(self.message)


class MissingHeaderException(Exception):
    """
    Header exception is an exception raised as a result of missing header values
    """

    def __init__(self, *args, **kwargs):
        invalid_header_error = ERROR_CODES.validation_errors.get('missing_header')

        self.message = invalid_header_error.message
        self.code = invalid_header_error.code

        if len(args) > 0:
            self.message = args[0]

        super(MissingHeaderException, self).__init__(self.message)


class MissingParametersError(Exception):
    """
    Missing parameter error is raised when an invalid json is provided to the system as input
    for json validation

    application.modules.core.exc.missing.MissingParametersError
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

    def __init__(self, *args, **kwargs):
        missing_parameters = ERROR_CODES.validation_errors.get('missing_parameter')

        self.message = missing_parameters.message
        self.code = missing_parameters.code

        if len(args) > 0:
            self.message = args[0]

        super(MissingParametersError, self).__init__(self.message)


class MismatchedParametersError(Exception):
    """
    Mismatched parameters error is raised when an invalid json is provided to the system as input
    for json validation

    application.modules.core.exc.missing.MismatchedParametersError
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

    def __init__(self, *args, **kwargs):
        mismatched_parameters = ERROR_CODES.validation_errors.get('mismatched_parameters')

        self.message = mismatched_parameters.message
        self.code = mismatched_parameters.code

        if len(args) > 0:
            self.message = args[0]

        super(MismatchedParametersError, self).__init__(self.message)


class MissingResourceError(Exception):
    """
    User not found error is raised when an invalid user id is provided to the system as input
    for user lookup

    application.modules.core.exc.missing.MissingResourceError
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

    def __init__(self, *args, **kwargs):
        missing_resource = ERROR_CODES.validation_errors.get('missing_resource')

        self.message = missing_resource.message
        self.code = missing_resource.code

        if len(args) > 0:
            self.message = args[0]

        super(MissingResourceError, self).__init__(self.message)


class ProviderNotFoundError(Exception):
    """
    Provider not found error is raised when an invalid provider id is provided to the system as input
    for provider lookup

    application.modules.core.exc.missing.ProviderNotFoundError
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

    def __init__(self, *args, **kwargs):
        user_not_found = ERROR_CODES.validation_errors.get('provider_not_found')

        self.message = user_not_found.message
        self.code = user_not_found.code

        if len(args) > 0:
            self.message = args[0]

        super(ProviderNotFoundError, self).__init__(self.message)


class ServiceNotFoundError(Exception):
    """
    Service not found error is raised when an invalid service name is provided to the system as input
    for service lookup in consul

    application.modules.core.exc.missing.ServiceNotFoundError
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

    def __init__(self, *args, **kwargs):
        service_not_found = ERROR_CODES.internal_errors.get('service_not_found')

        self.message = service_not_found.message
        self.code = service_not_found.code

        if len(args) > 0:
            self.message = args[0]

        super(ServiceNotFoundError, self).__init__(self.message)


class UserNotFoundError(Exception):
    """
    User not found error is raised when an invalid user id is provided to the system as input
    for user lookup

    application.modules.core.exc.missing.UserNotFoundError
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

    def __init__(self, *args, **kwargs):
        user_not_found = ERROR_CODES.internal_errors.get('user_not_found')

        self.message = user_not_found.message
        self.code = user_not_found.code

        if len(args) > 0:
            self.message = args[0]

        super(UserNotFoundError, self).__init__(self.message)
