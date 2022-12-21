from helper.Utilities import generate_random_email_and_password
from helper.requestsUtility import RequestsUtility


class Helper(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()

    def create_customer(self, email=None, password=None, **kwargs):

        if not email:
            random = generate_random_email_and_password()
            email = random['email']
        if not password:
            password = '123'

        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)

        rs_api = self.requests_utility.post('customers', payload=payload)
        return rs_api

    def get_product_by_id(self, product_id):
        return self.requests_utility.get(f"products/{product_id}")
