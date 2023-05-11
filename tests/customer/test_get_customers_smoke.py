import pytest
from helper_classes.requestsUtility import RequestsUtility
import logging


@pytest.mark.customers
@pytest.mark.tcid30
def test_get_all_customers():

    # make the call
    request_helper = RequestsUtility()
    rs_api = request_helper.get('customers')

    # verify status code of the call
    assert rs_api.status_code == 200, f'Expected status code 200 but actual {rs_api.status_code}'

    # verify get request is not an empty
    assert rs_api.json(), f"Response of a list all customers is empty"
