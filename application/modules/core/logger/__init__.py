"""
Application wide logger, could have used module based but making it trivial to re-implement for the whole team

application.modules.logger
~~~~~~~~~~~~~~~~~~~~~~~~~~

Logger module uses static programming language type syntax i.e. camelCase, don't know why they decided on that
but to keep the variables consistent naming convention follows the camelCase antecedent

Logging will be stored in a log server eventually where all logs can be viewed as required, this is why
the name of the microservice is important
"""
import os
import logging

#: Use the application config to control logging settings
from configuration import config
from configuration import APP_CONFIG, CURRENT_CONFIG

#: Get the environmental configuration or currently configured config
currentConfig = config.get(os.environ.get(APP_CONFIG) or CURRENT_CONFIG)

#: Necessary to differentiate these logs from logs from other micro services
#: especially when used by the service monitor to trace request path
applicationName = currentConfig.APP_NAME
logLevel = currentConfig.APP_LOG_LEVEL


logger = logging.getLogger(applicationName)
logger.setLevel(logLevel)

#: This can be redirected elsewhere for log recording
loggerHandler = logging.FileHandler(filename='application.log')
loggerHandler.setLevel(logLevel)


loggerFormatter = logging.Formatter('%(asctime)s -:::- %(name)s -:::- %(levelname)s -:::- %(message)s ')
loggerHandler.setFormatter(loggerFormatter)


logger.addHandler(loggerHandler)


def message_formatter(message, client):
    """
    Formats the message to a consistent format by logging the error and the causing client

    :param message:     The message to be formatted and worked upon
                        :type <type, 'str'>
    :param client:      The ip address of the client. can be replaced with transaction ID
                        :type <type, 'str'>
    :return message:    Properly formatted message consistent with the type necessary to provide best
                        information when inspected from a log file or log server whichever is used
                        :type <type, 'str'>
    """
    message = '{} : by {}'.format(message, client)
    return message


def message_logger(message, client):
    """
    Formats the message to a consistent format by logging the error and the causing client

    :param message:     The message to be formatted and worked upon
                        :type <type, 'str'>
    :param client:      The ip address of the client. can be replaced with transaction ID
                        :type <type, 'str'>
    :return message:    Properly formatted message consistent with the type necessary to provide best
                        information when inspected from a log file or log server whichever is used
                        :type <type, 'str'>
    """
    message = '{} : by {}'.format(message, client)
    return message
