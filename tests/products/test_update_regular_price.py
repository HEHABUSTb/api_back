import random
import pytest
from helper_classes.helper import Helper
from data_access_object.products_dao import ProductsDAO
from helper_classes.woo_api_utility import WooAPIUtility


@pytest.mark.tcid61
def test_update_regular_price():

    # call helper classes
    helper = Helper()
    woo_api = WooAPIUtility()

    # create test data
    random_product = ProductsDAO().get_random_product_from_db()
    random_product_id = random_product[0]['ID']
    random_price = f"{random.randint(10, 100)}.{random.randint(00, 100)}"

    # get old price
    product = woo_api.get(wc_endpoint=f"products/{random_product_id}")
    old_product_price = product['price']

    # make a PUT call for change price
    rs_api = helper.update_regular_price(product_id=random_product_id, payload={f"regular_price": f"{random_price}"})
    new_price = rs_api['price']

    # Verify response
    assert random_price == new_price, f"Price for product: {random_product_id} doesn't update." \
                                              f"should be {random_price} get {new_price}"
