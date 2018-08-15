"""
Tests autojsonify functions to make sure correctly formatted json responses are produced

tests.application.modules.api.rest.test_autojsonify
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import unittest

from application.modules._api.rest import autojsonify
from application.modules.core.exc.missing import MissingResourceError


FAILURE_CODE = 'A56900'
FAILURE_MESSAGE = 'Failed because you used too few tests'


class AutoJsonifyTest(unittest.TestCase):
    """
    AutoJsonifyTest Unittest implementing Class
    """

    def setUp(self):
        pass

    def test_autogenerate_failed_json(self):
        """
        Test that the autogenerate_failed_json message returns an error messge that is JSON rendered
        and ready.
        """
        __dummy_message = "Your resource is on holiday"
        __failed = "failed"

        sample_failed_json_message = autojsonify.auto_generate_failed_json(MissingResourceError(__dummy_message))
        failed = sample_failed_json_message.get("status")

        failed = failed == __failed

        self.assertIsInstance(sample_failed_json_message, dict)
        self.assertTrue(failed)
        self.assertDictContainsSubset({"message": __dummy_message}, sample_failed_json_message)

    def test_resolve_json_data_payload(self):
        """
        Tests that errors are raised or allowed values are returned from :meth `auto_return_value`

        :return:
        """
        self.assertRaises(ValueError, autojsonify.resolve_json_data_payload, 'What is happening?')
        self.assertRaises(ValueError, autojsonify.resolve_json_data_payload, 5)

        d = dict()
        l = [3]

        wrapped_dict = autojsonify.resolve_json_data_payload(d)
        wrapped_list = autojsonify.resolve_json_data_payload([3])
        null = autojsonify.resolve_json_data_payload(value=None)

        self.assertEqual(wrapped_dict, [d])
        self.assertEqual(wrapped_list, l)
        self.assertIsNone(null)

    def test_generate_denied_message(self):
        """
        Verifies success message generated from successful operation for correctness

        :return:
        """
        denied_json = autojsonify.generate_denied_message(FAILURE_MESSAGE, FAILURE_CODE)

        #: first assert there is no invalid nesting and is a valid json object
        self.assertIsNotNone(denied_json)
        self.assertIsInstance(denied_json, dict)

        wanted_json = {'status': 'failed', 'message': FAILURE_MESSAGE, 'error': FAILURE_CODE}
        self.assertDictContainsSubset(wanted_json, denied_json)

    def test_generate_failed_json(self):
        """
        Tests failure response from generate failed json message for correctness

        :return:
        """
        failed_json = autojsonify.generate_failed_json(FAILURE_MESSAGE, FAILURE_CODE)

        #: first assert it is a valid json object
        self.assertIsInstance(failed_json, dict)

        wanted_json = {'status': 'failed', 'message': FAILURE_MESSAGE, 'error': FAILURE_CODE}
        self.assertDictContainsSubset(wanted_json, failed_json)

    def test_generate_success_message(self):
        """
        Verifies success message generated from successful operation for correctness

        :return:
        """
        data = {'token': 'abcdefgh'}
        success_json = autojsonify.generate_success_message(data)

        #: first assert there is no invalid nesting and is a valid json object
        self.assertIsNotNone(success_json)
        self.assertIsInstance(success_json, dict)

        wanted_json = {'status': 'success', 'data': [data]}
        self.assertDictContainsSubset(wanted_json, success_json)
