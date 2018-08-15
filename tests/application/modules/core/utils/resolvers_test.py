"""
Resolvers Test Module

test.unit.application.modules.core.utils.resolvers_test
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Holds unit test functionality of the resolvers module
"""
import copy
from unittest import TestCase

from mock import Mock
import pytest

from application.constants import HAS_CAPS, HAS_EMPTY, HAS_LENGTH, HAS_NUMBER, HAS_SPACE, HAS_SYMBOL
from application.constants import NOT_EMPTY, NO_NUMBER, NO_SPACE, NO_SYMBOL
from application.modules.core.exc.invalid import InvalidValueError
from application.modules.core.exc.missing import MissingParametersError
from application.modules.core.utils import resolvers
from application.modules.core.utils.resolvers import validate_parameter_values


@pytest.mark.usefixtures('app_creation')
class ResolversTest(TestCase):
    def setUp(self):
        self.mock_get_request = Mock()
        self.mock_post_request = Mock()

        self.string_with_space = "My string with space"
        self.string_with_number = "mystring8"
        self.string_with_symbol = "me@you"
        self.string_empty = ""

        self.foolish_token = "thisDoesNotMeanAnything"
    
    def tearDown(self):
        pass
    
    def test_deserialize_token(self):
        pass
    
    def test_required_fields_present(self):
        required_fields = [
            ["a"],
            ["a", "aa"],
            ["a", "bb"],
            ["c"]
        ]
        json_payload = {
            "a": {
                "aa": True,
                "bb": "you gonna see"
            },
            "c": "can not be empty as well"
        }

        self.assertIsNone(resolvers.required_fields_present(required_fields, json_payload))

        required_fields = [["d"]]
        self.assertRaises(MissingParametersError, resolvers.required_fields_present, required_fields, json_payload)

    def test_private_validate_not_empty(self):
        """
        Tests to ensure that the :method `validate_not_empty` returns the appropriate
        response.
        Throws an InvalidValueError if the value failed validation and returns true otherwise
        :return:
        """
        validate_function = resolvers.validate_parameter_values
        self.assertRaises(AttributeError, validate_function, self.string_empty, [100])

        self.assertRaises(InvalidValueError, validate_function, self.string_empty, [NOT_EMPTY])
        self.assertRaises(InvalidValueError, validate_function, self.string_with_space, [NO_SPACE])
        self.assertRaises(InvalidValueError, validate_function, self.string_with_number, [NO_NUMBER])
        self.assertRaises(InvalidValueError, validate_function, self.string_with_symbol, [NO_SYMBOL])
        self.assertRaises(InvalidValueError, validate_function, self.string_with_symbol, [HAS_CAPS])
        self.assertRaises(InvalidValueError, validate_function, self.string_with_symbol, [HAS_EMPTY])
        self.assertRaises(InvalidValueError, validate_function, self.string_empty, [HAS_LENGTH])
        self.assertRaises(InvalidValueError, validate_function, self.string_with_symbol, [HAS_NUMBER])
        self.assertRaises(InvalidValueError, validate_function, self.string_with_symbol, [HAS_SPACE])
        self.assertRaises(InvalidValueError, validate_function, self.string_with_space, [HAS_SYMBOL])
    
    def test_resolve_request_params(self):
        """
        Test to make sure the :meth resolve_request_params works
        """
        valid_json_body = {'root': 'root_value', 'parent': 'parent_value'}
        self.mock_get_request.method = 'GET'
        self.mock_get_request.headers = valid_json_body

        self.mock_post_request.method = 'POST'
        self.mock_post_request.json = valid_json_body

        self.assertIsNotNone(resolvers.resolve_request_params(self.mock_get_request))
        self.assertIsInstance(resolvers.resolve_request_params(self.mock_post_request), dict)
