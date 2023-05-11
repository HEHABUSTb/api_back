import os
from helper_classes.host_config import WOO_API_HOSTS
from helper_classes.CredentialsUtility import CredentialsUtility
from woocommerce import API
import logging


class WooAPIUtility(object):

    def __init__(self):
        wc_creds = CredentialsUtility.get_wc_api_keys()
        self.env = os.environ.get('ENV', 'test')
        self.base_url = WOO_API_HOSTS[self.env]
        logging.info(f"Base url {self.base_url}")

        self.wcapi = API(
            url=self.base_url,
            consumer_key=wc_creds['wc_key'],
            consumer_secret=wc_creds['wc_secret'],
            version="wc/v3",
            timeout=30
        )

    @staticmethod
    def assert_status_code(expected_status_code, response_status_code):
        assert expected_status_code == response_status_code, f"Bat status code." \
                                                             f" Expected {expected_status_code} get {response_status_code}"

    def get(self, wc_endpoint, params=None, expected_status_code=200):

        rs_api = self.wcapi.get(wc_endpoint, params=params)
        rs_status_code = rs_api.status_code
        expected_status_code = expected_status_code
        rs_json = rs_api.json()
        self.assert_status_code(expected_status_code, rs_status_code)

        logging.info(f"Response GET code {rs_status_code}")
        logging.info(f"Response json {rs_json}")

        return rs_json

    def post(self, wc_endpoint, params=None, expected_status_code=200):

        rs_api = self.wcapi.post(wc_endpoint, data=params)
        rs_status_code = rs_api.status_code
        expected_status_code = expected_status_code
        rs_json = rs_api.json()
        self.assert_status_code(expected_status_code, rs_status_code)

        logging.info(f"Response POST code {rs_status_code}")
        logging.info(f"Response json {rs_json}")

        return rs_json

    def put(self, wc_endpoint, params=None, expected_status_code=200):

        rs_api = self.wcapi.put(wc_endpoint, data=params)
        rs_status_code = rs_api.status_code
        expected_status_code = expected_status_code
        rs_json = rs_api.json()
        self.assert_status_code(expected_status_code, rs_status_code)

        logging.info(f"Response PUT code {rs_status_code}")
        logging.info(f"Response json {rs_json}")

        return rs_json


if __name__ == '__main__':
    obj = WooAPIUtility()
    rs_api = obj.get('products')
    print(rs_api)
