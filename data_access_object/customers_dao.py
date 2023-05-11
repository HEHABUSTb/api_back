from helper_classes.DButility import DBUtility
import logging


class CustomersDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_customer_by_email(self, email):

        sql = f"SELECT * FROM site.wp_users where user_email = '{email}';"
        rs_sql = self.db_helper.execute_select(sql)
        logging.info(f'Execute {sql}')
        logging.info(f"Get a response {rs_sql}")

        return rs_sql

    def get_random_customer_from_db(self):

        sql = 'SELECT * FROM site.wp_users ORDER BY RAND() LIMIT 1;'
        rs_sql = self.db_helper.execute_select(sql)
        print(rs_sql)

        return rs_sql
