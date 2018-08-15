from unittest import TestCase

from application import create_app, db
from application.modules.core.exc.invalid import InvalidPageError, InvalidPageSizeError
from application.modules.core.utils.pagination import Paginator

class Doc(db.Document):
    index = db.IntField()

class TestPaginator(TestCase):

    def setUp(self):
        self.app = create_app("testing")

    def tearDown(self):
        Doc.drop_collection()

    def prep_collection(self, count=200):
        self.doc_count = count
        for i in xrange(self.doc_count):
            Doc(index=i).save()

        self.doc_qs = Doc.objects

    def test_init_raises_invalid_page_size_error(self):
        #test with empty collection
        self.prep_collection(0)
        with self.assertRaises(InvalidPageSizeError):
            paginator = Paginator(self.doc_qs, 0)

        #test with non-empty collection
        self.prep_collection(67)
        with self.assertRaises(InvalidPageSizeError):
            paginator = Paginator(self.doc_qs, 0)

    def test_set_and_get_current_page(self):
        self.prep_collection()
        page_size = self.doc_count/10
        #set current page to middle of pagination
        curr_page = self.doc_count/page_size/2 
        paginator = Paginator(self.doc_qs, page_size)

        paginator.set_current_page(curr_page)
        self.assertEqual(curr_page, paginator.current_page())

        #try with empty collection
        self.tearDown()
        self.prep_collection(0)
        self.doc_qs = Doc.objects
        page_size = 3
        paginator = Paginator(self.doc_qs, page_size)
        try:
            paginator.set_current_page(1)
            self.assertEqual(1, paginator.current_page())
        except Exception as e:
            self.fail("Could not set page number: {}".format(e))

        with self.assertRaises(InvalidPageError):
            paginator.set_current_page(2)
        with self.assertRaises(InvalidPageError):
            paginator.set_current_page(0)
        with self.assertRaises(InvalidPageError):
            paginator.set_current_page(-1)

    def test_current_page_queryset(self):
        self.prep_collection(100)
        page_size = 10

        #assert paginator sets current page to 1 by default
        paginator = Paginator(self.doc_qs, page_size)
        page_items = [doc.index for doc in list(paginator.current_page_queryset())]
        self.assertEqual(list(range(10)), page_items)

        curr_page = 10
        paginator = Paginator(self.doc_qs, page_size)
        paginator.set_current_page(curr_page)
        page_items = [doc.index for doc in list(paginator.current_page_queryset())]
        self.assertEqual(list(range(90, 100)), page_items)

        curr_page = 9
        page_size = 4
        paginator = Paginator(self.doc_qs, page_size)
        paginator.set_current_page(curr_page)
        page_items = [doc.index for doc in list(paginator.current_page_queryset())]
        self.assertEqual(list(range(32, 36)), page_items)

        #test page 1 when empty
        self.tearDown()
        self.prep_collection(0)
        page_size = 5
        paginator = Paginator(self.doc_qs, page_size)
        page_items = [doc.index for doc in list(paginator.current_page_queryset())]
        self.assertEqual(list(range(0)), page_items)

    def test_page_count(self):
        self.prep_collection(0)
        page_size = 10

        #empty collection page count
        paginator = Paginator(self.doc_qs, page_size)
        self.assertEqual(1, paginator.page_count())

        self.tearDown()
        self.prep_collection(101)
        page_size = 10
        paginator = Paginator(self.doc_qs, page_size)
        self.assertEqual(11, paginator.page_count())

        self.tearDown()
        self.prep_collection(109)
        page_size = 10
        paginator = Paginator(self.doc_qs, page_size)
        self.assertEqual(11, paginator.page_count())

        self.tearDown()
        self.prep_collection(2)
        page_size = 1
        paginator = Paginator(self.doc_qs, page_size)
        self.assertEqual(2, paginator.page_count())

        self.tearDown()
        self.prep_collection(1)
        page_size = 2
        paginator = Paginator(self.doc_qs, page_size)
        self.assertEqual(1, paginator.page_count())

    def test_has_next_and_previous_page(self):
        self.prep_collection(0)
        page_size = 10

        #empty collection has no other page
        paginator = Paginator(self.doc_qs, page_size)
        self.assertEqual(False, paginator.has_next_page())
        self.assertEqual(False, paginator.has_previous_page())

        self.tearDown()
        self.prep_collection(101)
        page_size = 10
        paginator = Paginator(self.doc_qs, page_size)
        paginator.set_current_page(1)
        self.assertEqual(True, paginator.has_next_page())
        self.assertEqual(False, paginator.has_previous_page())

        self.tearDown()
        self.prep_collection(101)
        page_size = 10
        paginator = Paginator(self.doc_qs, page_size)
        paginator.set_current_page(10)
        self.assertEqual(True, paginator.has_next_page())
        self.assertEqual(True, paginator.has_previous_page())

        self.tearDown()
        self.prep_collection(101)
        page_size = 10
        paginator = Paginator(self.doc_qs, page_size)
        paginator.set_current_page(11)
        self.assertEqual(False, paginator.has_next_page())
        self.assertEqual(True, paginator.has_previous_page())

    def test_next_and_previous_page_number(self):
        self.prep_collection(0)
        page_size = 10

        #empty collection has no other page
        paginator = Paginator(self.doc_qs, page_size)
        with self.assertRaises(InvalidPageError):
            paginator.next_page_number()
        with self.assertRaises(InvalidPageError):
            paginator.previous_page_number()

        self.tearDown()
        self.prep_collection(101)
        page_size = 10
        paginator = Paginator(self.doc_qs, page_size)
        paginator.set_current_page(1)
        self.assertEqual(2, paginator.next_page_number())
        with self.assertRaises(InvalidPageError):
            paginator.previous_page_number()

        self.tearDown()
        self.prep_collection(101)
        page_size = 10
        paginator = Paginator(self.doc_qs, page_size)
        paginator.set_current_page(10)
        self.assertEqual(11, paginator.next_page_number())
        self.assertEqual(9, paginator.previous_page_number())

        self.tearDown()
        self.prep_collection(101)
        page_size = 10
        paginator = Paginator(self.doc_qs, page_size)
        paginator.set_current_page(11)
        with self.assertRaises(InvalidPageError):
            paginator.next_page_number()
        self.assertEqual(10, paginator.previous_page_number())

    def test_pagination_info(self):
        self.prep_collection(0)
        page_size = 10

        #empty collection has no other page
        pagination_info = {
            "previous_page": None,
            "current_page": 1,
            "next_page": None,
            "page_count": 1
        }
        paginator = Paginator(self.doc_qs, page_size)
        self.assertEqual(pagination_info, paginator.pagination_info())

        self.tearDown()
        self.prep_collection(101)
        page_size = 10
        paginator = Paginator(self.doc_qs, page_size)
        paginator.set_current_page(1)
        pagination_info = {
            "previous_page": None,
            "current_page": 1,
            "next_page": 2,
            "page_count": 11
        }
        self.assertEqual(pagination_info, paginator.pagination_info())

        self.tearDown()
        self.prep_collection(101)
        page_size = 10
        paginator = Paginator(self.doc_qs, page_size)
        paginator.set_current_page(10)
        pagination_info = {
            "previous_page": 9,
            "current_page": 10,
            "next_page": 11,
            "page_count": 11
        }
        self.assertEqual(pagination_info, paginator.pagination_info())

        self.tearDown()
        self.prep_collection(101)
        page_size = 10
        paginator = Paginator(self.doc_qs, page_size)
        paginator.set_current_page(11)
        pagination_info = {
            "previous_page": 10,
            "current_page": 11,
            "next_page": None,
            "page_count": 11
        }
        self.assertEqual(pagination_info, paginator.pagination_info())