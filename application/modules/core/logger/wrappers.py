"""
Logbook package is responsible for all logging functionality in the application

application.modules.logbook.wrappers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Logs are necessary to inform development tracking and interaction monitoring
Without the logs the application would work fine, but then the question remains... How do
you have irrefutable knowledge of what exactly is happening between your application and the computer.
"""

import logging


def loggable(func):
    """
    Loggable function wraps any method that requires logging to occur semantically or functionally

    Logs are based on the log level and pertinent information is captured and logged automatically
    if loggable is used to decorate any method or function

    :param func:    The function to wrap
    :return:    Function wrapper
    """
    pass
