"""
This is the version one of the restful api

Register blueprints here, the blueprints hold and
expose their respective resources
"""
import re

from flask import g
from flask import request, jsonify

import autojsonify
from application.constants import (HTTP_UNSUPPORTED_MEDIA_TYPE,
                                   HTTP_UNAUTHORIZED, ONLY_JSON_MESSAGE)

from application.modules.core.exc.missing import MissingHeaderException
from application.modules.core.exc.missing import CredentialNotFoundError
from application.modules.core.exc.invalid import InvalidCredentialsError
from application.modules.churn_predictor import churn_blueprint_v1
from application.modules.core.utils.accessors import inspect_headers, check_authentication_token_in_redis
from application.modules.core.utils.resolvers import deserialize_token
from application.modules.core.utils.resolvers \
    import (resolve_authentication_string, resolve_token_privileges)



def allow_only_json():
    if request.method == 'POST' and not __is_json(request):
        return jsonify({
            "status": "failed",
            "message": ONLY_JSON_MESSAGE}),\
            HTTP_UNSUPPORTED_MEDIA_TYPE


def return_only_json(response):
    response.headers["Content-Type"] = "application/json"


def launch_all_api(app):
    app.register_blueprint(churn_blueprint_v1)
    

def validate_token():
    #: allow home page for documentation
    if request.path in ["/", "/static/rest.css"]:
        return

    if request.path.startswith("/v1/churn"):
        return



#    if re.match(r'(/v1/subscription.html/billing/(?P<account_name>.*)/confirm(?P<others>.*))', #request.path):
#        return

    try:
        authorization_dictionary = inspect_headers(request)
        authentication_string = authorization_dictionary.get("authorization")
        authentication_token = resolve_authentication_string(authentication_string)
        resolved_token = deserialize_token(authentication_token)
        resolve_token_privileges(request, authentication_token)
    except Exception as e:
        return autojsonify.json_failure(e)
        
    g.resolved_token = resolved_token


def __enable_sandbox(credential):
    pass


def __is_json(http_request):
    __APPLICATION_JSON = 'application/json'
    if not http_request.mimetype:
        return False
    return http_request.mimetype.lower() == __APPLICATION_JSON
