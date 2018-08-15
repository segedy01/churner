from application.constants.churned_data import CHURNED_DATA


def get_partners():
    partners = []
    for key, value in CHURNED_DATA.items():
        partners.append(key)

    return partners
