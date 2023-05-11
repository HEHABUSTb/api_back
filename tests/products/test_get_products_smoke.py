import pytest
from data_access_object.products_dao import ProductsDAO
from helper_classes.helper import Helper
import logging


@pytest.mark.products
@pytest.mark.tcid25
def test_get_all_products():

    # get a random product (test data) from db
    random_product = ProductsDAO().get_random_product_from_db(1)
    random_product_id = random_product[0]['ID']
    db_name_product = random_product[0]['post_title']

    # Make the call
    product_helper = Helper()
    rs_api = product_helper.get_product_by_id(random_product_id)
    rs_json = rs_api.json()
    api_name_product = rs_json['name']

    # verify status code of the call
    assert rs_api.status_code == 200, f'Expected status code 200 but actual {rs_api.status_code}'

    # verify response, not empty
    assert rs_api.json(), f"Response of a list all products is empty"

    # verify response, name of product
    logging.info(f"Products name in db {db_name_product} == {api_name_product}")
    assert db_name_product == api_name_product, f"Get product by id returned wrong product if: {random_product_id}" \
                                                f"db name: {db_name_product}, Api name {api_name_product}"
