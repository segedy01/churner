import math

from application.modules.core.exc.invalid import InvalidPageError, InvalidPageSizeError

class Paginator(object):
    """
    Create an abstraction of a pagination over mongoengine querysets.
    Sets the current page to the first page by default.

    A paginator is indexed from 1 to n pages where is the number of items in the
    queryset divided by the page size. For example if we have 100 items of page
    size 10 (10 items per page), the valid page numbers will be 1-10. If a 
    queryset contains no documents, then the paginator contains only one page 
    which is the empty page 1. 

    :param queryset: the mongoengine queryset to paginate over
    :param page_size: an integer greater than zero which will be the size of
        each page in the queryset except for the last page which might have a
        value less than page_size

    :raises InvalidPageSizeError: when the page_size is less than one, or if the 
        provided queryset is not a valid queryset.
    """
    def __init__(self, queryset, page_size):
        if page_size < 1:
            raise InvalidPageSizeError()

        self._queryset = queryset
        self._page_size = page_size

        self.set_current_page(1)

    def set_current_page(self, page_number):
        """
        Sets the 1-based index current page to work on. The page number x must
        be greater than zero.

        :page_number: the page number to set the pagination to

        :raises InvalidPageError: when the page number specified is invalid
        """
        page_count = self.page_count()
        if page_count == 0 and page_number == 1:
            self._current_page = page_number
            return

        if page_number < 1 or page_number > page_count:
            raise InvalidPageError()

        self._current_page = page_number

    def current_page(self):
        """
        Gets 1-based index of the current page in the pagination
        """
        return self._current_page

    def current_page_queryset(self):
        """
        Gets the queryset which includes all the items in the current page.

        :returns Queryset:
        """
        offset = self._page_size * (self.current_page() - 1)
        return self._queryset[offset : offset+self._page_size]

    def page_count(self):
        """
        Returns the number of pages present in the pagination
        """
        item_count = self._queryset.count()
        if item_count == 0:
            return 1
            
        return int(math.ceil(float(item_count) / self._page_size))

    def has_next_page(self):
        """
        Returns True if the pagination has a next page given the current page
        """
        return not (self.current_page() >= self.page_count())

    def next_page_number(self):
        """
        Gets the next page number after the current page in the pagination set

        :returns int: the next page number.

        :raises InvalidPageError: if there is no other page after the current one
        """
        if not self.has_next_page():
            raise InvalidPageError()
        return self._current_page + 1

    def has_previous_page(self):
        """
        Returns True if there is a valid page before the current page. False 
        otherwise.
        """
        return not (self.current_page() <= 1)

    def previous_page_number(self):
        """
        Gets the previous page number preceeding the current page in the pagination
        set.

        :returns int: the previous page number

        :raises InvalidPageError: if there is no page preceeding the current page
        """
        if not self.has_previous_page():
            raise InvalidPageError()
        return self.current_page() - 1

    def pagination_info(self):
        """
        Returns a dict of the format 
        {
            "previous_page": 3,
            "current_page": 4,
            "next_page": 5,
            "page_count": 10
        }

        In case of an invalid value for any of the fields, None is supplied.
        """
        pagination_info = {
            "previous_page": None,
            "current_page": None,
            "next_page": None,
            "page_count": None
        }
        if self.has_previous_page():
            pagination_info["previous_page"] = self.previous_page_number()

        if self.has_next_page():
            pagination_info["next_page"] = self.next_page_number()

        pagination_info["current_page"] = self.current_page()
        pagination_info["page_count"] = self.page_count()
        
        return pagination_info