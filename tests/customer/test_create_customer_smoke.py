import pytest
import logging
from helper.Utilities import generate_random_email_and_password
from helper.helper import Helper
from data_access_object.customers_dao import CustomersDAO


@pytest.mark.customers
@pytest.mark.tcid29
def test_create_create_customer_only_email_password():

    logging.info("TEST: Create new customer with email and password only")
    random = generate_random_email_and_password()
    email = random['email']
    password = random['password']

    # create payload
    payload = {'email': email, 'password': password}

    # make the call
    customer_helper = Helper()
    rs_api = customer_helper.create_customer(email=email, password=password)
    rs_json = rs_api.json()
    # import pdb
    # pdb.set_trace()

    # verify status code of the call
    assert rs_api.status_code == 201, f'Expected status code 201 but actual {rs_api.status_code}'

    # verify email in the response
    assert rs_json['email'] == email, f"Create customer API return wrong email. Expect {email}, get {rs_json['email']}"

    # verify first_name in json
    assert rs_json['first_name'] == '', f"Create customer api returned first_name {rs_json['first_name']} should be empty"

    # verify customer is created in database
    customer_dao = CustomersDAO()
    customer_info = customer_dao.get_customer_by_email(email)

    id_from_api = rs_json['id']
    id_from_db = customer_info[0]['ID']

    assert id_from_api == id_from_db, f"Create customer id from api {id_from_api} in database {id_from_db}"
