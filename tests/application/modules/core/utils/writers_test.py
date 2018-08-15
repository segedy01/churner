"""
Holds tests for the utils writers module
"""
from unittest import TestCase


from application.modules.core.utils import writers


class WritersTest(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_generate_authentication_token(self):
        """tests that authentication token genration works"""
        _token_dictionary = {"some": "dictionary"}
        authentication_token = writers.generate_authentication_token(_token_dictionary)

        self.assertGreater(len(authentication_token), 30)

    def test_populate_self_from_json(self):
        # model_instance = User()
        # collection = {"name": "musa", "email": "me@you.com"}
        # another_collection = {"name": "not musa"}
        #
        # writers.populate_self_from_json(model_instance, collection)
        #
        # collection_name = collection.get("name")
        # collection_email = collection.get("email")
        # another_collection_name = another_collection.get("name")
        #
        # self.assertEqual(model_instance.name, collection_name)
        # self.assertEqual(model_instance.email, collection_email)
        #
        # writers.populate_self_from_json(model_instance, another_collection, ["name"])
        # self.assertNotEqual(model_instance.name, another_collection_name)
        pass
