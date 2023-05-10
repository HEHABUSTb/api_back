import logging
import os
import json
from helper.woo_api_utility import WooAPIUtility


class OrdersHelper(object):

    def __init__(self):
        self.current_file_dir = os.path.dirname(__file__)
        self.payload_template = os.path.join(self.current_file_dir, '..', 'data', 'create_order_payload.json')
        self.woo_helper = WooAPIUtility()

    def create_order(self, additional_args=None):
        with open(self.payload_template) as file:
            payload = json.load(file)

        # if user add additional args, update payload
        if additional_args:
            assert isinstance(additional_args, dict), f"Parameter additional_args must be a dictionary not {type(additional_args)}"
            payload.update(additional_args)
        logging.info(f"Payload = {payload}")

        rs_api = self.woo_helper.post(wc_endpoint='orders', params=payload, expected_status_code=201)

        return rs_api
