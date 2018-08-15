"""
Test the application logging functionality of the application
"""


from unittest import TestCase
from application.modules.core.logger import logger, message_formatter


class LoggerTest(TestCase):
	"""
	Tests the logging utilities of the application
	"""

	def setUp(self):
		pass

	def test_message_formatter(self):
		"""
		Tests the message_formatter produces the expected output
		"""
		formatted_message = message_formatter("a", "b")
		self.assertIn("a : by b", formatted_message)
