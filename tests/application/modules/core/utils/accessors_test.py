"""
Accessors test module

tests.unit.application.modules.core.utils.accessors_test
"""
from datetime import datetime as clock
from unittest import TestCase
import pytest

from application.constants.testing import A_FAKE_TOKEN, A_FAKE_USER_ID, FAKE_APP_NAME

from application.modules.core.utils.writers import set_authentication_token_in_redis

from application.modules.core.utils import accessors
from application.modules.core.utils.accessors import has_privilege
from application.modules.core.utils.accessors import check_authentication_token_in_redis

from application.modules.core.exc.missing import UserNotFoundError
from application.modules.core.exc.missing import MissingResourceError
from application.modules.core.exc.missing import CredentialNotFoundError


@pytest.mark.usefixtures('app_creation')
class AccessorsTest(TestCase):
    """
    Accessors Test is used to test the functionality in accessors.
    """
    def setUp(self):
        """
        Setup the making fake data used.
        :return:
        """
        # self.client = User()
        # self.client.drop_collection()
        # self.client = Client(name="Voodata")
        # self.client.save()
        #
        # ClientCategory.drop_collection()
        # self.client_category = ClientCategory(name='small')
        # self.client_category.save()
        #
        # User.drop_collection()
        # self.user = User()
        # self.user.drop_collection()
        # self.user.name = "Superuser"
        # self.user.password_hash = "ieiakejdkklajdlkajkla"
        # self.user.account = self.client
        # self.user.save()
        #
        # Applicant.drop_collection()
        # self.applicant = Applicant()
        # self.applicant.email = "applicant@joblivery.com"
        # self.applicant.date_of_birth = clock.now()
        pass

    def tearDown(self):
        """
        Teardown the clear/delete the fake data used.
        :return:
        """
        # self.client.drop_collection()
        # self.user.drop_collection()
        # self.applicant.drop_collection()
        pass

    def test_get_account_or_404(self):
        """
        Test to make sure the get_account_or_404 works.
        :return:
        """
        # _small = "small"
        # account_info = Account.objects(name=_small)
        # self.assertIsNotNone(account_info)
        # self.assertRaises(MissingResourceError, get_account_or_404, unique_identifier='no_such_event')
        pass

    def test_get_credential_or_404(self):
        """
        Test to make sure the get_credential_or_404 works.
        :return:
        """
        # self.assertRaises(CredentialNotFoundError, accessors.get_credential_or_404, A_FAKE_USER_ID)
        pass

    def test_get_user_or_404(self):
        """
        Test to make sure the get_user_or_404 works.
        :return:
        """
        # user = User.objects(name=self.user.name)
        # self.assertIsNotNone(user)
        # self.assertRaises(UserNotFoundError, get_user_or_404, user_id='no_such_user')
        pass

    def test_check_authentication_token_in_redis(self):
        """
        Tests to make sure that the authentication token is readable from redis

        This check authentication in redis logically, and sensibly depends on set authentication token in redis
        as a result the test for the set authentication token in redis handles testing that function even though
        the function is used here to set an authentication token in redis
        :return:
        """
        set_authentication_token_in_redis(A_FAKE_TOKEN, FAKE_APP_NAME)
        token_in_redis = check_authentication_token_in_redis(A_FAKE_TOKEN, FAKE_APP_NAME)
        self.assertIsNotNone(token_in_redis)

    def test_get_service_ip_address_from_service_registry(self):
        """
        Tests to ensure that consul is a reliable store for micro service ip and addressing information
        as to enable service discovery
        """
        #: TODO implement this test unfailingly
        pass

    def test_has_privilege(self):
        """
        Tests that the user has privileges to perform the action at the supposed endpoint
        """
        _credential = {
            "privileges": {
                "orders": {
                    "view": False,
                    "create": True
                }
            }
        }
        _endpoint = "orders"
        _method = "POST"
        _put = "PUt"

        self.assertIsNotNone(has_privilege(_credential, _method, _endpoint))
        self.assertTrue(has_privilege(_credential, _method, _endpoint))
        self.assertFalse(has_privilege(_credential, _put, _endpoint))
