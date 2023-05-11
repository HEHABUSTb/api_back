from helper_classes.DButility import DBUtility
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

    def get_product_by_id(self, product_id):

        sql = f"SELECT * FROM site.wp_posts WHERE ID = {product_id}"
        rs_sql = self.db_helper.execute_select(sql)
        logging.info(f'Execute {sql}')
        logging.info(f"Get a response {rs_sql}")

        return rs_sql

    def get_products_created_after_given_date(self, _date):

        sql = f"SELECT * FROM site.wp_posts WHERE post_type = 'product' AND post_date > '{_date}' AND post_status = 'publish';"
        rs_sql = self.db_helper.execute_select(sql)
        logging.info(f'Execute {sql}')
        logging.info(f"Get a response {rs_sql}")

        return rs_sql


if __name__ == "__main__":
    result = ProductsDAO().get_product_by_id(62)
    print(result)
