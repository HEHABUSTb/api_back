import logging
import os
import json
from helper.woo_api_utility import WooAPIUtility
from data_access_object.order_dao import OrderDAO


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
            assert isinstance(additional_args, dict),\
                f"Parameter additional_args must be a dictionary not {type(additional_args)}"
            payload.update(additional_args)
        logging.info(f"Payload = {payload}")

        rs_api = self.woo_helper.post(wc_endpoint='orders', params=payload, expected_status_code=201)

        return rs_api

    def update_order(self, order_id, payload):
        return self.woo_helper.put(f"orders/{order_id}", payload)

    @staticmethod
    def verify_order_is_created(order_json, expected_products, customer_id=0):
        order_dao = OrderDAO()

        # Verify response

        assert order_json, f"Create order response is empty"
        assert order_json['customer_id'] == customer_id, f"Expected Customer_id {customer_id} " \
                                                             f"but get {order_json['customer_id']}"
        len_items = len(order_json['line_items'])
        expected_len = len(expected_products)
        order_id = order_json['id']
        assert len_items == expected_len, f"Expected only {expected_len} item in order get: {len_items}," \
                                          f" Order id: {order_id}"

        # verify db
        order_item_from_response = order_json['line_items']
        # logging.info(f"{order_item_from_response}")
        item_from_response = order_item_from_response[0]['name']
        len1 = len(order_item_from_response[0]['name'])
        logging.info(f"{len1}")
        logging.info(f"Item name from response: {item_from_response}")

        order_items = order_dao.get_order_item_by_order_id(order_id=order_id)
        # logging.info(f"Items from db: {order_items}")
        items = [i for i in order_items if i['order_item_type'] == 'line_item']
        item_from_db = items[0]['order_item_name']
        logging.info(f"Items from db: {item_from_db}")

        assert len(items) == 1, f"Expected only 1 item get: {len(items)}"
        assert item_from_response == item_from_db, f"Order Items from response {item_from_response}" \
                                                   f" not equal order items from db {item_from_db}"
