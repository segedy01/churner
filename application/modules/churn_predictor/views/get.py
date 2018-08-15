from flask import request, jsonify
from .. import churn_blueprint_v1

from ..controllers import get

GET = ['GET']

@churn_blueprint_v1.route('/v1/churn/partners', methods=GET)
def get_partners():
    try:
        response = get.get_partners()
    except Exception as e:
        return json_failure(e)
    return jsonify(success=True, data=response), 200