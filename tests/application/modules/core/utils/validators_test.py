from unittest import TestCase

from application.modules.core.utils.validators import is_phone_valid

class TestValidators(TestCase):
    def test_is_phone_valid(self):
        #test mtn numbers
        mtn_numbers = ['07031342940', '07061542940']