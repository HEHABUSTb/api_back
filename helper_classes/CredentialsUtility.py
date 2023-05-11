import os


class CredentialsUtility(object):

    def __init__(self):
        pass

    @staticmethod
    def get_wc_api_keys():

        wc_key = os.environ.get('WC_KEY')
        wc_secret = os.environ.get('WC_SECRET')

        if not wc_key or not wc_secret:
            raise Exception('The API credentials WC_KEY and WC_SECRET must be in env variables')
        else:
            return {'wc_key': wc_key, 'wc_secret': wc_secret}

    @staticmethod
    def get_db_credentials():

        db_user = 'root'
        db_password = 'root'
        db_host = '127.0.0.1'
        db_port = int(3306)

        return {'db_user': db_user, 'db_password': db_password, 'db_host': db_host, 'db_port': {db_port}}
