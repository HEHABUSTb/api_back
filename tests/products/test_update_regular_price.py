from helper_classes.helper import Helper


def test_update_regular_price():
    helper = Helper()

    # choose random product
    product_id = 63
    payload = {"regular_price": "24.54"}

    # make a call
    rs_api = helper.update_regular_price(product_id=63)
    p = 1

    # Verify response