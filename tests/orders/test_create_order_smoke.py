import pytest

from data_access_object.products_dao import ProductsDAO
from helper_classes.orders_helper import OrdersHelper
from helper_classes.helper import Helper
import logging


@pytest.fixture
def setup_product_id():
    product_dao = ProductsDAO()

    # get a random product from db
    random_product = product_dao.get_random_product_from_db(quantity=1)
    product_id = random_product[0]['ID']
    logging.info(f"Random product id: {product_id}")

    return product_id


@pytest.mark.orders
@pytest.mark.tcid48
def test_create_paid_order_guest_user(setup_product_id):

    order_helper = OrdersHelper()
    product_id = setup_product_id

    # make the call
    info = {"line_items": [{"product_id": product_id, "quantity": 1}]}
    order_json = order_helper.create_order(additional_args=info)
    order_id = order_json['id']
    products = order_json['line_items']
    logging.info(f"Order id: {products}")
    logging.info(f"Order id: {order_id}")

    # Verify response and db
    order_helper.verify_order_is_created(order_json, products, customer_id=0)


@pytest.mark.orders
@pytest.mark.tcid49
def test_create_paid_order_new_customer():
    product_dao = ProductsDAO()
    order_helper = OrdersHelper()
    customer_helper = Helper()

    # get a product from db
    random_product = product_dao.get_random_product_from_db(quantity=1)
    product_id = random_product[0]['ID']
    logging.info(f"Random product id {product_id}")

    # Create new customer
    new_customer = customer_helper.create_customer().json()
    new_customer_id = new_customer['id']

    # make the call
    info = {"line_items": [{"product_id": product_id, "quantity": 1}], "customer_id": new_customer_id}
    order_json = order_helper.create_order(additional_args=info)
    order_id = order_json['id']
    products = order_json['line_items']
    logging.info(f"Order id: {products}")
    logging.info(f"Order id: {order_id}")

    # Verify response and db
    order_helper.verify_order_is_created(order_json, products, customer_id=new_customer_id)
