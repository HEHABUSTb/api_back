import pytest
from helper.requestsUtility import RequestsUtility
import logging


@pytest.mark.products
@pytest.mark.tcid24
def test_get_all_products():

    # make the call
    request_helper = RequestsUtility()
    rs_api = request_helper.get(endpoint='products')

    # verify status code of the call
    assert rs_api.status_code == 200, f'Expected status code 200 but actual {rs_api.status_code}'

    # verify get request is not an empty
    assert rs_api.json(), f"Response of a list all products is empty"
