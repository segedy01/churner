"""
 Dev-Utils Test Module

test.unit.application.modules.core.utils.dev_utils
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Holds unit test functionality of the resolvers module
"""

from application.modules.core.utils.dev_utils import get_user_id
from unittest import TestCase
from flask import g
from application import create_app
import json



class DevUtilsTest(TestCase):

    def setUp(self):
        self.app = create_app('testing', validate_tokens=False)
        self.test_client = self.app.test_client()

    def tearDown(self):
        pass

    def test_get_user_id_with_json_dumps(self):
        user_id = json.dumps({'user_id': 'dale@job.com'})
        resolved_token = {'data': user_id}

        with self.app.app_context():
            g.resolved_token = resolved_token
            result = get_user_id()
            self.assertEquals(result, 'dale@job.com')

    def test_get_user_id(self):
        user_id = {'user_id': 'dale@job.com'}
        resolved_token = {'data': user_id}

        with self.app.app_context():
            g.resolved_token = resolved_token
            result = get_user_id()
            self.assertEquals(result, 'dale@job.com')