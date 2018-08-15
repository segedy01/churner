from flask import Blueprint
from flask_cors import CORS

churn_blueprint_v1 = Blueprint("churn", __name__)
CORS(churn_blueprint_v1)
from views import get
from views import post
