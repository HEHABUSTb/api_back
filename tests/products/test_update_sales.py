import pytest
import logging
from helper_classes.woo_api_utility import WooAPIUtility
from helper_classes.Products_helper import ProductsHelper
import random


@pytest.mark.tcid63
def test_update_sale_price():
    helper = WooAPIUtility()

    # Get product with on_sale = False
    product_id = 21

    product = helper.get(wc_endpoint="products/21")
    product_sale = product['on_sale']
    if product_sale is True:
        helper.put(wc_endpoint="products/21", params={"sale_price": ""})
        product = helper.get(wc_endpoint="products/21")

    # Add sale_price

    product_sale_status = product['on_sale']
    product_sale_price = product['sale_price']
    assert product_sale_status is False, f"Product sale status should be a False, not a {product_sale}"
    assert product_sale_price == "", f"Product sale price should be empty not a {product_sale_price}"

    regular_price = product['regular_price']
    sale_price = float(regular_price) * 0.75
    payload = {"sale_price": "{:.2f}".format(sale_price)}

    updated_product = helper.put(wc_endpoint="products/21", params=payload)
    product_sale_status = updated_product['on_sale']

    # Verify response
    assert product_sale_status is True, f"Product sale status should be a True, not a {product_sale_status}"

    # Remove sale_price


def test_update_sale_price2():
    helper = ProductsHelper()
    product_id = 21
    product = helper.step_remove_sale_price(product_id=product_id)
    helper.step_update_sale_price(product=product)
    helper.step_remove_sale_price(product_id=product_id)
