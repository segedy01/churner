"""
Test that the HTTP code constants do not change arbitarily as certain tests may
depend on them
"""

from application.constants.codes.http import *

HTTP_GOOD_REQUEST_TEST = 200  #: You did a Good job, so We did a good job. Give us more requests like this
HTTP_CREATED_TEST = 201   #: We have created the resource you wanted us to create
HTTP_ACCEPTED_TEST = 202  #: Your request is with us, We have agreed to work on it when we can
HTTP_NO_CONTENT_TEST = 204  #: Resource deleted and the server has no cotent to display
HTTP_BAD_REQUEST_TEST = 400   #: Your request is a crime against http
HTTP_UNAUTHORIZED_TEST = 401  #: Are you sure you are authenticated
HTTP_NOT_FOUND_TEST = 404  #: You are looking for aliens or something else that does not exist
HTTP_NOT_ALLOWED_TEST = 405   #: No no no, that is not part of our agreement
HTTP_TIMEOUT_TEST = 408   #: We ran out of patience with your request
HTTP_PRECONDITION_FAILED_TEST = 412
HTTP_UNSUPPORTED_MEDIA_TYPE_TEST = 415    #: We can not continue down this path with you. Bad content type
HTTP_UNPROCESSABLE_ENTITY_TEST = 422  #: Nice work but you are spitting garbage
HTTP_NOT_IMPLEMENTED_TEST = 501   #: The action is not implemented on this server
HTTP_BAD_GATEWAY_TEST = 502   #: Something happened on our way to the backend service
HTTP_SERVICE_UNAVAILABLE_TEST = 503  #: Self provided service is not available
HTTP_GATEWAY_TIMEOUT_TEST = 504  #: We could not wait for a response because our time and your time is valuable to us


def test_http_codes():
    assert HTTP_GOOD_REQUEST_TEST == HTTP_GOOD_REQUEST
    assert HTTP_CREATED_TEST == HTTP_CREATED
    assert HTTP_ACCEPTED_TEST == HTTP_ACCEPTED
    assert HTTP_NO_CONTENT_TEST == HTTP_NO_CONTENT
    assert HTTP_BAD_REQUEST_TEST == HTTP_BAD_REQUEST
    assert HTTP_UNAUTHORIZED_TEST == HTTP_UNAUTHORIZED
    assert HTTP_NOT_FOUND_TEST == HTTP_NOT_FOUND
    assert HTTP_NOT_ALLOWED_TEST == HTTP_NOT_ALLOWED
    assert HTTP_TIMEOUT_TEST == HTTP_TIMEOUT
    assert HTTP_PRECONDITION_FAILED_TEST == HTTP_PRECONDITION_FAILED
    assert HTTP_UNSUPPORTED_MEDIA_TYPE_TEST == HTTP_UNSUPPORTED_MEDIA_TYPE
    assert HTTP_UNPROCESSABLE_ENTITY_TEST == HTTP_UNPROCESSABLE_ENTITY
    assert HTTP_NOT_IMPLEMENTED_TEST == HTTP_NOT_IMPLEMENTED
    assert HTTP_BAD_GATEWAY_TEST == HTTP_BAD_GATEWAY_TEST
    assert HTTP_SERVICE_UNAVAILABLE_TEST == HTTP_SERVICE_UNAVAILABLE
    assert HTTP_GATEWAY_TIMEOUT_TEST == HTTP_GATEWAY_TIMEOUT
