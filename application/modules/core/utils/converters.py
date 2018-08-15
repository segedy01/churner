"""
Converters modules holds the utility helper methods for conversion and transformation
across different EDI (Electronic data interchange formats)

application.modules.core.utils.converters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import json
import ast
import mongoengine
from bson import ObjectId
from datetime import datetime

# import xmltodict
# from xml.parsers.expat import ExpatError

from application.modules.core.exc.invalid import InvalidParametersError
from application.modules.core.exc.invalid import InvalidResponseError

from application.modules.core.logger import logger


def get_dictionary_value_using_nested_list(nested_list, dictionary, offset=None):
    """Throws key error if item not found
    Using the :param `nested_list` get the dictionary value at an appropriate nesting of
    items from left to right.

    :param nested_list:         Collection of keys ordered from left to right where the leftmost
                                value corresponds to the root key and every subsequent value represents
                                a nested key and so on continuously according to the length of the collection
                                :type <type, 'list'>


    :param dictionary:          Json resolvable dictionary collection of key value pairs to be traversed according
                                to the ordering of keys in the list for value retrieval.
                                :type <type, 'dict'>

    :param offset:              Used to determine the current object in scope to use for value setting
                                and is especially useful when a list of objects is encountered with repeated
                                object local matching nested keys.
                                :type <type, 'int'>

    :return wanted_value:       The value to return to the calling context which is of a type corresponding
                                to one of the valid json types and valid fetchr allowed data interchange format types
                                :type <type, 'object'>
    """
    if not offset:
        offset = 1

    #: Make offset a real based index as opposed to zero based index
    #: to enable intuitive actual position lookups
    offset -= 1
    dictionary = dictionary.copy()
    for key_name in nested_list:
        dictionary = dictionary[key_name.encode('utf-8')]
        if isinstance(dictionary, list):
            dictionary = dictionary[offset]

    return dictionary


def set_dictionary_value_using_nested_list(value, nested_list, dictionary, offset=None):
    """
    Using the :param `nested_list` set the dictionary value at and using the params at an appropriate nesting of
    items from left to right.

    :param value:               The value to set to the calling context which is of a type corresponding
                                to one of the valid json types and valid fetchr allowed data interchange format types
                                :type <type, 'object'>

    :param nested_list:         Collection of keys ordered from left to right where the leftmost
                                value corresponds to the root key and every subsequent value represents
                                a nested key and so on continuously according to the length of the collection
                                :type <type, 'list'>

    :param dictionary:          Json resolvable dictionary collection of key value pairs to be traversed according
                                to the ordering of keys in the list for value retrieval.
                                :type <type, 'dict'>

    :param offset:              Used to determine the current object in scope to use for value setting
                                and is especially useful when a list of objects is encountered with repeated
                                object local matching nested keys.
                                :type <type, 'int'>

    :return populated_dict:     Dictionary populated after traversal of input dictionary
                                :type <type, 'dict'>
    """
    if not offset:
        offset = 1
    offset -= 1
    print "dictionary==",list(dictionary)
    # dictionary = dictionary.copy()
    # : Extract dictionary values by using nested list
    for key_name in nested_list[:-1]:
        dictionary = dictionary[key_name.encode('utf-8')]
        if isinstance(dictionary, list):
            dictionary = dictionary[offset]
    dictionary[nested_list[-1]] = value
    return dictionary