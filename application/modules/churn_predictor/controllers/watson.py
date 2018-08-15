import requests
import json
from application.modules.core.exc.failed import InternalServerError


class Watson():
    def __init__(self, token, url):
        self.header = {'Authorization': 'Bearer {}'.format(token), 'Content-Type': 'application/json' }
        self.url = url

    def predict_churn(self, data):
        print self.header
        response = requests.post(self.url, json=data, headers=self.header)
        return response


