import pytest
import logging

from data_access_object.products_dao import ProductsDAO
from helper_classes.orders_helper import OrdersHelper


@pytest.fixture
def setup_product_id():
    product_dao = ProductsDAO()

    # get a random product from db
    random_product = product_dao.get_random_product_from_db(quantity=1)
    product_id = random_product[0]['ID']
    logging.info(f"Random product id: {product_id}")

    return product_id


@pytest.mark.tcid60
def test_create_order_with_coupon(setup_product_id):

    order_helper = OrdersHelper()
    product_id = setup_product_id
    coupon = {"code": "50off2"}

    # make the call
    info = {"line_items": [{"product_id": product_id, "quantity": 1}],
            "coupon_lines": [coupon]}

    order_json = order_helper.create_order(additional_args=info)
    order_id = order_json['id']
    products = order_json['line_items']
    logging.info(f"Order id: {products}")
    logging.info(f"Order id: {order_id}")

    # Verify response and db
    order_helper.verify_order_is_created(order_json, products, customer_id=0)