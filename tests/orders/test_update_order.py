from helper.orders_helper import OrdersHelper
import pytest
import logging


@pytest.mark.tcid55
def test_update_order_status():

    expected_status = 'cancelled'
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
