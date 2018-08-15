from unittest import TestCase

from application import create_app

class BaseTester(TestCase):
    def setUp(self, config_val="testing", validate_tokens=False):
        self.app = create_app(config_val, validate_tokens=validate_tokens)

    def tearDown(self):
        #perfom very generic cleanup
        pass