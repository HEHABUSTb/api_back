import logging
from helper_classes.Utilities import generate_random_string
from helper_classes.helper import Helper
from data_access_object.products_dao import ProductsDAO
import pytest


@pytest.mark.tcid26
@pytest.mark.products
def test_create_one_simple_product():

    # generate data
    payload = dict()
    payload['name'] = generate_random_string()
    logging.info(f"Random name {payload['name']}")
    payload['type'] = "simple"
    payload['regular_price'] = "9.99"

    # make the call
    rs_api = Helper().call_create_product(payload=payload)
    rs_json = rs_api.json()
    rs_name = rs_json['name']

    # verify response code
    assert rs_api.status_code == 201, f'Expected status code 201 but actual {rs_api.status_code}'

    # verify response is not empty
    assert rs_api.json(), f"Response of a list all products is empty"
    assert payload['name'] == rs_name, f"Unexpected name in response get {rs_json['name']} should {rs_name}"

    # verify existing in db
    rs_id_product = rs_json['id']
    database_product = ProductsDAO().get_product_by_id(rs_id_product)
    db_name = database_product[0]['post_title']

    assert payload['name'] == db_name, f"DataBase name doesn't match expect {payload['name']} in database {db_name}"

    # delete simple product
    logging.info(f'Deleting product.... by id {rs_id_product}')
    rs_api = Helper().delete_product_by_id(rs_id_product)

    # verify response code
    assert rs_api.status_code == 200, f'Expected status code 200 but actual {rs_api.status_code}'

    # verify response is not empty
    assert rs_api.json(), f"Response of a list all products is empty"

    # verify trashed in db
    database_product = ProductsDAO().get_product_by_id(rs_id_product)
    db_post_status = database_product[0]['post_status']
    assert db_post_status == "trash", f"Expected product in trash get {db_post_status} from db"
