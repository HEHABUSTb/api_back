import pytest
from data_access_object.products_dao import ProductsDAO
from helper.orders_helper import OrdersHelper

@pytest.mark.tcid48
def test_create_paid_order_guest_user():
    product_dao = ProductsDAO()
    order_helper = OrdersHelper()

    # get a product from db
    random_product = product_dao.get_random_product_from_db(quantity=1)
    product_id = random_product[0]['ID']
    order_helper.create_order()

    # make the call

    # verify response

    # verify db