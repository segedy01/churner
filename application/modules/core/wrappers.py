"""
Core wrappers module contains utility classes and wrapper functions for import and reuse project wide

application.modules.core.wrappers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


class LookupDict(dict):
    """
    A Dictionary object that enables looking up of properties using object access protocol

    In addition to providing the normal dict key syntax i.e. `dict['key']` the LookupDict
    enables retrieval of dict values using object access protocol i.e. `dict.key` to enable
    easy traversal and access to values from external callers
    """
    def __init__(self, *args, **kwargs):
        super(LookupDict, self).__init__(*args, **kwargs)

    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value


__all__ = [
    'LookupDict'
]
