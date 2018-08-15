# --*-- coding: utf8 --*--
import os
import logging


APP_CONFIG = 'APP_CONFIG'
APP_NAME = 'Entree'

CURRENT_CONFIG = 'development'
#: Let's see again

DB_HOST = 'localhost'
DB_NAME = "EntreeDB"
DB_PORT = 27017  #: default port of the database vendor

DEV_DB_HOST = DB_HOST
DEV_DB_NAME = "devEntreeDB"
DEV_DB_PORT = DB_PORT  #: change if different from default port

STAGING_DB_HOST = DB_HOST
STAGING_DB_NAME = "stagingEntreeDB"
STAGING_DB_PORT = DB_PORT  #: change if different from default port

TEST_DB_HOST = DB_HOST
TEST_DB_NAME = "testEntreeDB"
TEST_DB_PORT = DB_PORT  #: change if different from default port


class Config(object):
    """
    Config class holds application defaults to be used in production environment
    """
    APP_LOG_LEVEL = logging.INFO
    APP_NAME = APP_NAME

    DEBUG = False
    ENVIRONMENT = 'production'

    JSONIFY_PRETTYPRINT_REGULAR = True
    JSON_SORT_KEYS = False

    DB_NAME = DB_NAME
    DB_HOST = os.environ.get('DB_HOST', DB_HOST)
    DB_PORT = int(os.environ.get('DB_PORT', DB_PORT))

    MONGODB_DB = DB_NAME
    MONGODB_HOST = DB_HOST
    MONGODB_PORT = DB_PORT
    MONGODB_USERNAME = os.environ.get('ENTREE_DB_USERNAME')
    MONGODB_PASSWORD = os.environ.get('ENTREE_DB_PASSWORD')

    #: SANDBOX_PREFIX = "sandbox-"
    SECRET_KEY = os.environ.get('SECRET_KEY')


class StagingConfig(object):
    APP_LOG_LEVEL = logging.INFO
    APP_NAME = APP_NAME

    DEBUG = False
    ENVIRONMENT = 'staging'

    JSONIFY_PRETTYPRINT_REGULAR = True
    JSON_SORT_KEYS = False

    DB_NAME = STAGING_DB_NAME
    DB_HOST = os.environ.get('STAGING_DB_HOST') or STAGING_DB_HOST
    DB_PORT = os.environ.get('STAGING_DB_PORT') or STAGING_DB_PORT

    SECRET_KEY = os.environ.get('STAGING_SECRET_KEY')


class DevelopmentConfig(object):
    """
    DevelopmentConfig class holds application defaults to be used in development environment
    """
    APP_LOG_LEVEL = logging.DEBUG
    APP_NAME = APP_NAME

    DEBUG = True
    ENVIRONMENT = 'development'

    JSONIFY_PRETTYPRINT_REGULAR = True
    JSON_SORT_KEYS = False

    DB_NAME = DEV_DB_NAME
    DB_HOST = os.environ.get('DEV_DB_HOST') or DEV_DB_HOST
    DB_PORT = os.environ.get('DEV_DB_PORT') or DEV_DB_PORT

    MONGODB_DB = DEV_DB_NAME
    MONGODB_HOST = DB_HOST
    MONGODB_PORT = DB_PORT

    SECRET_KEY = os.environ.get('DEV_SECRET_KEY') or 'ju5t_f0r_D3VeLopm#nt_T#1s_!s_okay'


class TestingConfig(object):
    """
    TestingConfig class holds application defaults to be used in testing environment
    """
    APP_LOG_LEVEL = logging.INFO
    APP_NAME = APP_NAME

    DEBUG = True
    ENVIRONMENT = 'testing'

    JSONIFY_PRETTYPRINT_REGULAR = True
    JSON_SORT_KEYS = False

    DB_NAME = TEST_DB_NAME
    DB_HOST = os.environ.get('TEST_DB_HOST') or TEST_DB_HOST
    DB_PORT = os.environ.get('TEST_DB_PORT') or TEST_DB_PORT

    MONGODB_DB = TEST_DB_NAME
    MONGODB_HOST = TEST_DB_HOST
    MONGODB_PORT = TEST_DB_PORT

    SECRET_KEY = os.environ.get('TEST_SECRET_KEY') or 'ju5t_f0r_T3St1ng_T#1s_!s_okay'


prod_config = Config
config = {
    'production': Config,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'default': DevelopmentConfig
}
