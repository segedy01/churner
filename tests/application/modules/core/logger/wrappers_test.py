"""
Test wrapper functionalities
"""


from unittest import TestCase

from application.modules.core.logger import wrappers


class WrappersTest(TestCase):
	"""
	Forgotten what wrappers was about but nothing goes untested here
	"""

	def setUp(self):
		pass

	def test_loggable(self):
		"""
		Tests the loggable function performs as is expected
		"""
		is_loggable = wrappers.loggable("pass_in_a_function_at_implementation")
		self.assertIsNone(is_loggable)
