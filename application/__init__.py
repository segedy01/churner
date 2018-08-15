"""
Application initialization file
"""
import os

import markdown
import jinja2
from flask import Flask, Response
from flask_mongoengine import MongoEngine
from redis import StrictRedis
from flask_cors import CORS

import configuration
import constants


db = MongoEngine()
rdb = StrictRedis()

API_DOC_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            font-family: sans-serif;
        }
        code, pre {
            font-family: monospace;
        }
        h1 code,
        h2 code,
        h3 code,
        h4 code,
        h5 code,
        h6 code {
            font-size: inherit;
        }
        h1 {
            margin-top: 100px;
            font-weight: 700
        }
        h1:first-of-type {
            margin-top: 20px;
        }
        h2 {
            margin-top:50px
        }
    </style>
</head>
<body>
<div class="container">
{{content}}
</div>
</body>
</html>
"""

def apidoc():
    with open(os.path.join(os.path.dirname('..'),'api.md')) as f:
        md = f.read()
        extensions = ['extra', 'smarty']
        html = markdown.markdown(md, extensions=extensions, output_format='html5')
        return jinja2.Template(API_DOC_TEMPLATE).render(content=html)

def create_app(config_string, validate_tokens=True):
    app = Flask(__name__)
    cfg = configuration.config.get(config_string)
    app.config.from_object(cfg)

    db.init_app(app)

    #: launch all views in the application by launching the api launcher (lol)
    #: version three api imported in create app to prevent circular dependencies
    #: when redis :object `rdb` is imported from any where in the application
    #: this is because the api accesses and registers the blueprint views which reference
    #: controllers which in turn reference the rdb. Life is bliss isn't it?
    from modules._api.rest import version_three
    version_three.launch_all_api(app)

    #: restrict post requests to json only
    app.before_request(version_three.allow_only_json)
    if validate_tokens:
        app.before_request(version_three.validate_token)

    @app.route("/", methods=["GET"])
    def home():
        return Response(apidoc(), mimetype='text/html')

    @app.route('/.well-known/acme-challenge/<token_value>')
    def letsencrpyt(token_value):
        with open(os.path.join(os.path.dirname('..'),
            '.well-known/acme-challenge/{}'.format(token_value))) as f:
            answer = f.readline().strip()
            print answer
        return answer

    return app