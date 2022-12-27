import pytest
from datetime import datetime, timedelta
from helper.helper import Helper
import logging
from data_access_object.products_dao import ProductsDAO


@pytest.mark.regression
class TestListProductsWithFilter(object):

    @pytest.mark.tcid51
    def test_list_products_with_filter_after(self):

        # create data
        x_days_from_today = 30
        payload = dict()
        after_created_date = datetime.now().replace(microsecond=0) - timedelta(days=x_days_from_today)
        after_created_date = after_created_date.isoformat()
        payload['after'] = after_created_date
        payload['per_page'] = 10
        logging.info(f"Date time for test {payload['after']}")

        # make the call
        rs_api = Helper().call_list_products(payload)
        rs_status_code, rs_json = rs_api
        logging.info(f"{rs_status_code} \n {rs_json}")

        # verify response status code
        assert rs_status_code == 200, f'Expected status code 200 but actual {rs_status_code}'

        # get data from db
        db_products = ProductsDAO().get_products_created_after_given_date(after_created_date)
        db_products_number = len(db_products)
        rs_number_products = len(rs_json)

        # verify response match db
        assert rs_number_products == db_products_number, f"List of products with filter 'after' returned wrong value" \
                                                       f"Expected {db_products_number} get {rs_number_products}"

        ids_products_in_api = set([product['id'] for product in rs_json])
        ids_products_in_db = set([product['ID'] for product in db_products])
        logging.info(f"ids from api {ids_products_in_api}")
        logging.info(f"ids from db {ids_products_in_db}")

        ids_diff = list(ids_products_in_api - ids_products_in_db)

        assert not ids_diff, f"List of products ids with filter 'after' from api mismatch with db {ids_diff}"
