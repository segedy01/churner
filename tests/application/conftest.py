"""
Configuration shared setup module

tests.unit.application.conftest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module is used to share setup across all sub packages and modules
to reduce the need for multiple instantiation of expensive functionality
"""
import pytest

from application import create_app


#: @pytest.mark.usefixtures('app_creation')


@pytest.fixture()
def app_creation():
    app = create_app('testing')
    app.app_context().push()
    app.test_request_context().push()
