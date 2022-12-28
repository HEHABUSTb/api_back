import os
import json


class OrdersHelper(object):

    def __init__(self):
        self.current_file_dir = os.path.dirname(__file__)
        self.payload_template = os.path.join(self.current_file_dir, '..', 'data', 'create_order_payload.json')

    def create_order(self, additional_args=None):
        with open(self.payload_template) as file:
            payload = json.load(file)
            import pdb; pdb.set_trace()
