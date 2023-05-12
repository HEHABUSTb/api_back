import random

from helper_classes.helper import Helper
import logging


class ProductsHelper(Helper):
    def __init__(self):
        super().__init__()

    def step_remove_sale_price(self, product_id):
        logging.info('step_remove_sale_price')
        product = self.woo_helper.get(wc_endpoint=f"products/{product_id}")
        product_sale = product['on_sale']
        if product_sale is True:
            self.woo_helper.put(wc_endpoint="products/21", params={"sale_price": ""})
            product = self.woo_helper.get(wc_endpoint=f"products/{product_id}")

        product_sale_status = product['on_sale']
        product_sale_price = product['sale_price']
        logging.info(f'on_sale status is {product_sale_status} sale_price = {product_sale_price}')
        assert product_sale_status is False, f"Product sale status should be a False, not a {product_sale}"
        assert product_sale_price == "", f"Product sale price should be empty not a {product_sale_price}"

        return product

    def step_setup_sale_price(self, product_id):
        logging.info('step_setup_sale_price')

        product = self.woo_helper.get(wc_endpoint=f"products/{product_id}")

        # Create payload
        regular_price = product['regular_price']
        sale_price = float(regular_price) * 0.75
        payload = {"sale_price": "{:.2f}".format(sale_price)}

        # Update product sale_price
        updated_product = self.woo_helper.put(wc_endpoint=f"products/{product_id}", params=payload)
        product_sale_status = updated_product['on_sale']

        # Verify response
        assert product_sale_status is True, f"Product sale status should be a True, not a {product_sale_status}"

    def step_update_sale_price(self, product_id, multiple=2):
        logging.info('step_update_sale_price')

        while multiple > 0:
            logging.info(f"Start loop update multiple number: {multiple}")
            product = self.woo_helper.get(wc_endpoint=f"products/{product_id}")
            old_sale_price = product['sale_price']
            regular_price = product['regular_price']

            # Create payload
            percent = float(f"0.{random.randint(1, 99)}")
            sale_price = float(regular_price) * percent
            payload = {"sale_price": "{:.2f}".format(sale_price)}

            # Update product sale_price
            updated_product = self.woo_helper.put(wc_endpoint=f"products/{product_id}", params=payload)
            product_sale_status = updated_product['on_sale']
            new_sale_price = updated_product['sale_price']

            # Verify response
            logging.info(f"Old sale_price: {old_sale_price} new sale_price: {new_sale_price}")
            assert product_sale_status is True, f"Product sale status should be a True, not a {product_sale_status}"
            assert new_sale_price != old_sale_price, f"Expected different values for sale_price old: {old_sale_price}" \
                                                     f" new: {new_sale_price}"
            multiple -= 1
