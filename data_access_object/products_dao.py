from helper.DButility import DBUtility
import logging
import random


class ProductsDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_random_product_from_db(self, quantity=1):

        sql = "SELECT * FROM site.wp_posts where post_type = 'product' limit 100;"
        rs_sql = self.db_helper.execute_select(sql)
        logging.info(f'Execute {sql}')
        logging.info(f"Get a response {rs_sql}")

        return random.sample(rs_sql, int(quantity))


if __name__ == "__main__":
    f = ProductsDAO()
    f.get_random_product_from_db()
