from helper_classes.Utilities import generate_random_string
from helper_classes.orders_helper import OrdersHelper
import pytest
import logging

pytestmark = [pytest.mark.orders, pytest.mark.regression]


@pytest.mark.tcid55
@pytest.mark.tcid56
@pytest.mark.tcid57
@pytest.mark.parametrize("expected_status",
                        [
                            pytest.param('cancelled', marks=[pytest.mark.tcid55, pytest.mark.smoke]),
                            pytest.param('completed', marks=pytest.mark.tcid56),
                            pytest.param('on-hold', marks=pytest.mark.tcid57)
                        ])
def test_update_order_status(expected_status):

    # expected_status = 'cancelled'
    logging.info(f"expected_status = {expected_status}")
    orders_helper = OrdersHelper()

    # create new order
    order_json = orders_helper.create_order()
    order_id = order_json['id']
    logging.info(f"Order id {order_id}")
    current_status = order_json['status']

    assert current_status != expected_status, f"Current status of order is already {expected_status}"

    # Update the status
    payload = {"status": expected_status}
    updated_order = orders_helper.update_order(order_id=order_id, payload=payload)

    # Verify status of an order
    updated_status = updated_order['status']
    logging.info(f"Check status of an order expected_status = {expected_status}, updated_status = {updated_status}")
    assert expected_status == updated_status, f"Expected order status: {expected_status} not: {updated_status}"


@pytest.mark.tcid58
def test_update_invalid_order_status():

    expected_status = 'hardcore'
    logging.info(f"expected_status = {expected_status}")
    orders_helper = OrdersHelper()

    # create new order
    order_json = orders_helper.create_order()
    order_id = order_json['id']
    logging.info(f"Order id {order_id}")
    current_status = order_json['status']
    logging.info(f"Current order status {current_status}")

    # Try Update the status
    payload = {"status": expected_status}
    rs_api = orders_helper.update_order(order_id=order_id, payload=payload, expected_status_code=400)

    # Verify response information
    expected_code = 'rest_invalid_param'
    current_code = rs_api['code']
    assert current_code == expected_code,\
        f"Update order status to random string didn't have correct code in response. " \
        f"Expected: {expected_code}, get: {current_code}"

    expected_message = 'Invalid parameter(s): status'
    current_message = rs_api['message']
    assert expected_message == current_message, f"Update order status to random string didn't have correct message." \
                                                f"Expected: {expected_message} get: {current_message} "


@pytest.mark.tcid59
def test_update_order_customer_note():

    orders_helper = OrdersHelper()

    # create new order
    order_json = orders_helper.create_order()
    old_customer_note = order_json['customer_note']
    logging.info(f"Old customer note: {old_customer_note}")
    order_id = order_json['id']
    logging.info(f"Order id: {order_id}")

    # Update customer note
    random_string = generate_random_string(length=40)
    payload = {"customer_note": random_string}
    updated_order = orders_helper.update_order(order_id=order_id, payload=payload)
    updated_customer_note = updated_order['customer_note']

    assert random_string == updated_customer_note, f"Updated customer note: {updated_customer_note}" \
                                                       f" is not equal random customer note {random_string}"
