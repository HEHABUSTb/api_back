import pytest

from data_access_object.order_dao import OrderDAO
from data_access_object.products_dao import ProductsDAO
from helper.orders_helper import OrdersHelper
import logging


@pytest.mark.tcid48
def test_create_paid_order_guest_user():
    product_dao = ProductsDAO()
    order_dao = OrderDAO()
    order_helper = OrdersHelper()

    # get a product from db
    random_product = product_dao.get_random_product_from_db(quantity=1)
    product_id = random_product[0]['ID']
    logging.info(f"Random product id {product_id}")

    # make the call
    info = {"line_items": [{"product_id": product_id, "quantity": 1}]}
    order_json = order_helper.create_order(additional_args=info)
    order_id = order_json['id']
    logging.info(f"Order id: {order_id}")

    # verify response
    assert order_json, f"Create order response is empty"
    assert order_json['customer_id'] == 0, f"customer_id not a guest should be 0 get: {order_json['customer_id']}"
    len_items = len(order_json['line_items'])
    assert len_items == 1, f"Expected only 1 item in order get: {len_items}, Order id: {order_json['id']}"

    # verify db
    order_item_from_response = order_json['line_items']
    #logging.info(f"{order_item_from_response}")
    item_from_response = order_item_from_response[0]['name']
    logging.info(f"Item name from response: {item_from_response}")

    order_items = order_dao.get_order_item_by_order_id(order_id=order_id)
    #logging.info(f"Items from db: {order_items}")
    items = [i for i in order_items if i['order_item_type'] == 'line_item']
    item_from_db = items[0]['order_item_name']
    logging.info(f"Items from db: {item_from_db}")

    assert len(items) == 1, f"Expected only 1 item get: {len(items)}"
    assert item_from_response == item_from_db, f"Order Items from response {item_from_response}" \
                                               f" not equal order items from db {item_from_db}"
