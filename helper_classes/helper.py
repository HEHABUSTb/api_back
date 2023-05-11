from helper_classes.Utilities import generate_random_email_and_password
from helper_classes.requestsUtility import RequestsUtility
from woo_api_utility import WooAPIUtility
import logging


class Helper(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()
        self.woo_helper = WooAPIUtility()

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

    def call_create_product(self, payload):
        return self.requests_utility.post('products', payload=payload)

    def call_list_products(self, payload=None):

        max_pages = 1000
        all_products = []

        for i in range(1, max_pages + 1):
            logging.info(f"List of products page number {i}")

            payload['page'] = i
            rs_api = self.requests_utility.get('products', payload=payload)
            status_code = rs_api.status_code
            rs_json = rs_api.json()

            # if there is no response stop the loop, there are no more products
            if not rs_json:
                logging.info(f"Page number {i} is empty break the loop")
                break
            else:
                all_products.extend(rs_json)
        else:
            raise Exception(f"Unable to find all products after {max_pages} pages")

        return status_code, all_products

    def delete_product_by_id(self, product_id):
        return self.requests_utility.delete(f"products/{product_id}")

    def update_regular_price(self, product_id, payload):
        return self.woo_helper.put(f"products/{product_id}", params=payload)
