import requests
import os
from helper.host_config import API_HOSTS
import logging


class RequestsUtility(object):

    def __init__(self):
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]

    def post(self, endpoint, payload=None, headers=None):

        if not headers:
            headers = {"Content-Type": "application/json"}

        url = self.base_url + endpoint
        logging.info(f'url for the post call: {url}')

        import json
        payload = json.dumps(payload)
        logging.info(f'payload for the post call: {payload}')

        rs_api = requests.post(url=url, data=payload, headers=headers)
        import pdb; pdb.set_trace()

    def get(self):
        pass


if __name__ == "__main__":
    requests1 = RequestsUtility()
    payload = {'email': 'test_user_ykzpnvfvrf@gmail.com', 'password': 'crcwafbvkv'}
    requests1.post('customers', payload)
