from flask import request, jsonify
from .. import churn_blueprint_v1
from application.modules._api.rest.autojsonify import json_failure

from ..controllers import post

POST = ['POST']

@churn_blueprint_v1.route('/v1/churn', methods=POST)
def predict_churn():
    try:
        json_data = request.json
        response = post.get_prediction(json_data)
    except Exception as e:
        print(e)
        return json_failure(e)
    return jsonify(success=True, data=response), 200