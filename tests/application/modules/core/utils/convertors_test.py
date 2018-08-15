"""
Convertors Test Module

test.unit.application.modules.core.utils.convertors_test
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Holds unit test functionality of the convertors module
"""
import copy
from unittest import TestCase


from mock import Mock


from application.constants.testing import (FAKE_NESTED_DICTIONARY, FAKE_NESTED_LIST_ONE, FAKE_NESTED_LIST_ONE_RESULT,
    FAKE_NESTED_LIST_TWO, FAKE_NESTED_LIST_TWO_RESULT, FAKE_NESTED_LIST_TWO_RESULT_B)

from application.modules.core.exc.invalid import InvalidParametersError
from application.modules.core.exc.missing import ProviderNotFoundError
from application.modules.core.exc.invalid import InvalidResponseError

from application.modules.core.utils import converters


class ConvertorsTest(TestCase):
    """
    Convertors will convert the xml message body to dict.
    """
    def setUp(self):
        """
        set up fake data instead setting it over and over.
        :return:
        """
        self.mock = Mock()
        self.mock_http_request = Mock()
        self.mock_http_request.json = {
            "courier_provider": {
                "courier_provider_id": 22,
                "courier_provider_name": "Sridevi"
            }
        }

        self.value = 'Yippee Ka Yay'
        self.sample_nested_list_one = FAKE_NESTED_LIST_ONE
        self.expected_value_one = FAKE_NESTED_LIST_ONE_RESULT

        self.sample_nested_list_two = FAKE_NESTED_LIST_TWO
        self.expected_value_two = FAKE_NESTED_LIST_TWO_RESULT
        self.expected_value_two_b = FAKE_NESTED_LIST_TWO_RESULT_B
        self.sample_nested_list_dictionary = FAKE_NESTED_DICTIONARY

    def tearDown(self):
        """
        Tear down will clear every db collection which we created using test.
        :return:
        """
        pass

    def test_get_dictionary_value_using_nested_list(self):
        """
        Ensure that a dictionary value nested according to the items of a list can be looked up given
        a list that has a linear representation of its nesting
        :return:
        """
        snl_one = self.sample_nested_list_one
        snl_two = self.sample_nested_list_two
        snl_dict = self.sample_nested_list_dictionary

        wanted_value = converters.get_dictionary_value_using_nested_list(snl_one, snl_dict)
        self.assertIsNotNone(wanted_value)
        self.assertEquals(wanted_value, self.expected_value_one)

        wanted_value = converters.get_dictionary_value_using_nested_list(snl_two, snl_dict)
        self.assertIsNotNone(wanted_value)
        self.assertEquals(wanted_value, self.expected_value_two)

        wanted_value = converters.get_dictionary_value_using_nested_list(snl_two, snl_dict, offset=2)
        self.assertIsNotNone(wanted_value)
        self.assertEquals(wanted_value, self.expected_value_two_b)

    def test_set_dictionary_value_using_nested_list(self):
        """
        Ensure that a dictionary value nested according to the items of a list can be changed given
        a list that has a linear representation of its nesting
        :return:
        """
        snl_one = self.sample_nested_list_one
        snl_two = self.sample_nested_list_two
        snl_dict = self.sample_nested_list_dictionary

        wanted_dictionary = converters.set_dictionary_value_using_nested_list(self.value, snl_one, snl_dict)
        self.assertIsNotNone(wanted_dictionary)
        self.assertIsInstance(wanted_dictionary, dict)
        new_value = converters.get_dictionary_value_using_nested_list(snl_one, snl_dict)

        #: now Yippee kai yay
        self.assertEquals(self.value, new_value)
