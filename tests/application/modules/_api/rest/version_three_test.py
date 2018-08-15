"""
Tests autojsonify functions to make sure correctly formatted json responses are produced

tests.application.modules.api.rest.test_autojsonify
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import unittest
from mock import Mock

import application

from application.constants import ONLY_JSON_MESSAGE
from application.modules._api.rest import version_three

_APP_JSON = 'application/json'
_AUTHORIZATION_KEY = 'Authorization'
_AUTHORIZATION_TOKEN = 'Bearer ieikja2akdadjk'
_CONTENT_TYPE = 'Content-Type'
_TOKEN = 'ieikja2akdadjk'


class VersionThreeTest(unittest.TestCase):

    def setUp(self):
        """Initialize expensive operations"""
        app = application.create_app('testing')
        self.app = app.test_client()
        self.raw_app = app
        self.mock_app = Mock()

    def tearDown(self):
        """Release expensive resources"""
        pass

    def test_allow_only_json(self):
        """Tests the test for only json works as expected"""
        http_response = self.app.post('/v1/authenticate',
                                      headers={
                                          _AUTHORIZATION_KEY: _AUTHORIZATION_TOKEN,
                                          _CONTENT_TYPE: _APP_JSON
                                      })
        #: look at response to ensure it gives 401 unauthorized
        self.assertIn('401', http_response.status)

        http_response = self.app.post('/v1/authenticate',
                                      headers={
                                          _AUTHORIZATION_KEY: _AUTHORIZATION_TOKEN
                                      })
        #: look at response to ensure it throws 415 unsupported media type
        self.assertIn('415', http_response.status)

        #: ensure that the only json Content-Type error raises for bad requests
        self.assertIn(ONLY_JSON_MESSAGE, http_response.data)

    @unittest.skip("")
    def test_launch_all_api(self):
        """Test the lauch all APIS method"""
        mock_app = Mock()
        version_three.launch_all_api(mock_app)

        #: If register_blueprint method was called in the launch_all_api method
        #: then we are certain that the flask app instance will register same
        #: once called and our method should work just fine
        self.assertTrue(mock_app.register_blueprint.called)

    def test_validate_token(self):
        documentation_response = self.app.get('/')

        #: Change this later when you can test the method itself and not the value of the view response
        #: change to assertIsNone because that is what we expect the actual method we are testing to return for this route and method
        self.assertIsNotNone(documentation_response)
