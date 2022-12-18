import pytest
import logging as logger
from helper.Utilities import generate_random_email_and_password
from helper.customer_helper import CustomerHelper


@pytest.mark.tcid29
def test_create_create_customer_only_email_password():

    logger.info("TEST: Create new customer with email and password only")
    random = generate_random_email_and_password()
    email = random['email']
    password = random['password']

    # create payload
    payload = {'email': email, 'password': password}

    # make the call
    customer_helper = CustomerHelper()
    customer_api_info = customer_helper.create_customer(email=email, password=password)
    # import pdb;
    # pdb.set_trace()

    # verify status code of the call

    # verify email in the response

    # verify customer is created in database
