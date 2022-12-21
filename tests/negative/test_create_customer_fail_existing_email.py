import pytest
import logging
from data_access_object.customers_dao import CustomersDAO
from helper.helper import Helper


@pytest.mark.customers
@pytest.mark.tcid47
def test_create_customer_fail_existing_email():

    # get existing email from db
    customer_dao = CustomersDAO()
    existing_customer = customer_dao.get_random_customer_from_db()
    existing_email = existing_customer[0]['user_email']

    # call the api
    customer_helper = Helper()
    rs_api = customer_helper.create_customer(email=existing_email, password='Password1')
    rs_json = rs_api.json()

    # verify status code of the call
    assert rs_api.status_code == 400, f'Expected status code 400 but actual {rs_api.status_code}'

    # verify code in response
    assert rs_json['code'] == 'registration-error-email-exists', f"Wrong code should be" \
                                                                 f" 'registration-error-email-exists'" \
                                                                 f"get {rs_json['code']}"

    # verify message in response
    expected_message = 'An account is already registered with your email address.' \
                       ' <a href="#" class="showlogin">Please log in.</a>'
    assert rs_json['message'] == expected_message, f"Wrong message should be {expected_message}" \
                                                   f" get {rs_json['message']}"
