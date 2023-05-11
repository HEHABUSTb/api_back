from helper_classes.DButility import DBUtility
import logging


class OrderDAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_order_item_by_order_id(self, order_id=87):

        sql = f"SELECT * FROM site.wp_woocommerce_order_items WHERE order_id = {order_id};"
        rs_sql = self.db_helper.execute_select(sql)
        logging.info(f'Execute {sql}')
        logging.info(f"Get a response {rs_sql}")

        return rs_sql


if __name__ == "__main__":
    result = OrderDAO().get_order_item_by_order_id()
    print(result)
