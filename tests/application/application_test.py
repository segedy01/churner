import unittest

from flask import Flask
from configuration import prod_config
from application import create_app


PRODUCTION = 'production'
DEVELOPMENT = 'development'
ERROR_MSG = 'Environment Configuration Mismatch'


class ApplicationTest(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_create_app_returns_flask_app(self):
        """
        Tests to ensure that a flask application is returned on callling :meth `create_app`
        :return:
        """
        production_app = create_app(PRODUCTION)
        self.assertIsInstance(production_app, Flask)

        development_app = create_app(DEVELOPMENT)
        self.assertIsInstance(development_app, Flask)

        #: Ensure that development keyword gives an app that runs with development settings
        self.assertTrue(development_app.config.get('DEBUG'))
        self.assertEquals(development_app.config.get('ENVIRONMENT'), DEVELOPMENT, ERROR_MSG)

        #: Ensure that production keyword gives an app that runs with production settings
        self.assertFalse(production_app.config.get('DEBUG'))
        self.assertEquals(production_app.config.get('ENVIRONMENT'), PRODUCTION, ERROR_MSG)

        #: Invalid environment name passed to flask application should cause an error to be raised
        self.assertRaises(TypeError, create_app('wrong environment name'))
