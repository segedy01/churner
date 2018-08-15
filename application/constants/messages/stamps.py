"""
Messages constants hold messages that are used in more than one place
to provide a single point of change

application.constants.messages.stamps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Candidate for refactoring: move all constant messages here or export __all__
"""

BAD_CREDENTIALS_STAMP = "Invalid credentials provided to system by "
BUSY_RESOURCE_STAMP = "Request sent when internal service down, by "

DUPLICATE_ORDER_STAMP = "Duplicate order was tried to be saved by "
DUPLICATE_USER_STAMP = "Duplicate user was tried to be saved by "

INVALID_ORDER_STAMP = "Invalid order was tried to be saved by {}"
INVALID_USER_STAMP = "Invalid data provided for user creation by {}"
INVALID_JSON_VALUES_STAMP = "Invalid order was tried to be saved by {}"
INSUFFICIENT_PRIVILEGES_STAMP = "Unauthorized request to higher privileged resource by {}"

MISSING_PARAMETER_STAMP = "Bad Request with missing parameters sent by "

NEW_ORDER_CREATED_STAMP = "A new user was created successfully by "
NEW_USER_CREATED_STAMP = "A new user was created successfully by "
NO_JSON_FOUND_STAMP = "Why are you sending empty json requests?"
NO_MICROSERVICE_STAMP = "{} microservice is unavailable"

ONLY_POST_STAMP = "Only POST methods allowed for this resource"

RABBIT_UNAVAILABLE_STAMP = "Sorry! Our code is on strike, try later"
RABBIT_UNRESPONSIVE_STAMP = "Sorry! All our code workers are busy, try later"

SIMILAR_USER_STAMP = "Similar user exists on the system"

USELESS_JSON_STAMP = "How do we say this, your JSON is useless, add appropriate keys"


__all__ = [
    'BAD_CREDENTIALS_STAMP',
    'DUPLICATE_ORDER_STAMP',
    'DUPLICATE_USER_STAMP',
    'INSUFFICIENT_PRIVILEGES_STAMP',
    'INVALID_ORDER_STAMP',
    'INVALID_JSON_VALUES_STAMP',
    'INVALID_USER_STAMP',
    'BUSY_RESOURCE_STAMP',
    'MISSING_PARAMETER_STAMP',
    'NEW_ORDER_CREATED_STAMP',
    'NEW_USER_CREATED_STAMP',
    'NO_JSON_FOUND_STAMP',
    'NO_MICROSERVICE_STAMP',
    'ONLY_POST_STAMP',
    'RABBIT_UNAVAILABLE_STAMP',
    'RABBIT_UNRESPONSIVE_STAMP',
    'SIMILAR_USER_STAMP',
    'USELESS_JSON_STAMP'
]
