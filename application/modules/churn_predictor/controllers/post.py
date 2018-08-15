from application.constants.churned_data import CHURNED_DATA
from application.constants.churned_data import TOKEN, URL
from application.modules.core.exc.missing import MissingResourceError
from application.modules.churn_predictor.controllers.watson import Watson
from collections import deque

def get_prediction(request_data):
    partner_data = CHURNED_DATA.get(request_data.get('partner', ''))
    if not partner_data:
        partner_data = request_data.get('data')
        total_health = partner_data.get('resource') + partner_data.get('finance') + partner_data.get('quality') + partner_data.get('concern')
        partner_data.update({'cummulative_health': int(total_health)})
    if not partner_data:
        message = 'Resource Does Not Exist'
        raise MissingResourceError(message)

    mr_watson = Watson(TOKEN, URL)
    partner_data_title = []
    partner_data_value = []
    for key, value in partner_data.items():
        partner_data_title.append(key)
        partner_data_value.append(value)
    data = {
        "fields": partner_data_title,
        "values": [partner_data_value]
    }
    print "===================================================================================="
    print "===================================================================================="
    print "===================================================================================="
    print data
    print "===================================================================================="
    print "===================================================================================="
    print "===================================================================================="
    response = mr_watson.predict_churn(data)
    res = response.json()
    print(res)
    probability_of_churn = res.get('values')[0][-1]
    partner_data['probability_of_churn'] = probability_of_churn
    return partner_data

