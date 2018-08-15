#!/usr/bin/env python

import os

from flask_mongoengine import MongoEngine
from flask_script import Manager
from flask_script import Server
from flask_script import Shell

from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

from application import create_app
from application import db
from configuration import DB_NAME, DEV_DB_NAME, DB_PORT, DEV_DB_PORT


app = create_app(os.environ.get('APP_CONFIG') or 'development')
manager = Manager(app)


def make_shell_context():
    """
    Makes a context object to use for the shell environment exposed by flask-script
    :return context:    Context object containing environmental defaults
                        :type <type, 'dict'>

    >>> from flask import Flask
    >>> response = make_shell_context()
    >>> isinstance(response, dict)
    True

    >>> app = response.get('app')
    >>> isinstance(app, Flask)
    True

    >>> db = MongoEngine(app)
    >>> isinstance(db, MongoEngine)
    True
    """
    return dict(app=app, db=db)


manager.add_command('runserver', Server(host='127.0.0.1', port='9060', use_debugger=True, use_reloader=True))
manager.add_command('shell', Shell(make_context=make_shell_context))

@manager.command
def initdb():
    """
    Initializes the database with values necessary for rapid usability feedback

    :return initialized:    Boolean value specifying the status of the initialization
                            operation | function
                            :type <type, 'bool'>

    >>> initdb()
    True
    """
    #: Get the current environment of execution
    environment = os.environ.get('APP_CONFIG')
    joblivery_port = os.environ.get('DB_PORT') or DB_PORT
    joblivery_host = os.environ.get('DB_HOST') or DB_HOST

    if joblivery_host and joblivery_port and (environment=='production'):
        initialized = __initialize_db(DB_NAME)
    else:
        initialized = __initialize_db(DEV_DB_NAME)

    #: As always no news is good news philosophy preferred
    if not initialized:
        print 'Database Initialization Failed: Check To Ensure MongoDB Is Installed and Running'
    return initialized


@manager.command
def dropdb():
    """
    Drops the database with values necessary for rapid usability feedback

    :return dropped:        Boolean value specifying the status of the initialization
                            operation | function
                            :type <type, 'bool'>

    >>> dropdb()
    True
    """
    #: Get the current environment of execution
    environment = os.environ.get('APP_CONFIG')

    if environment == 'production':
        dropped = __drop_db(DB_NAME)
    else:
        dropped = __drop_db(DEV_DB_NAME)

    #: As always no news is good news philosophy preferred
    if not dropped:
        print 'Database Drop Failed: Ensure DB Exists and MongoDB Is Running'
    return dropped


@manager.command
def populatedb():
    """
    Populates the mongodb database with default values especially for testing purposes

    :return:
    """
    from mongoengine import connect
    pass


def __initialize_db(database_name):
    """
    Private helper method to initialize a MongoDB database and prevent small but still same old
    code repetition
    """
    connection = MongoClient(serverSelectionTimeoutMS=10000)
    initialization_collection = 'initialization'
    try:
        new_db = connection[database_name]
        if not initialization_collection in new_db.collection_names():
            new_db.create_collection(initialization_collection)
    except ServerSelectionTimeoutError as sste:
        return False
    return True


def __drop_db(database_name):
    """
    Drops the databases created

    :param database_name:   The name of the database to drop
    """
    try:
        from mongoengine import connect
        dbs = connect(database_name)
        dbs.drop_database(database_name)
    except ValueError:
        return False
    return True

application = app

if __name__ == '__main__':
    manager.run()
