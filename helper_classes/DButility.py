import pymysql
from helper.CredentialsUtility import CredentialsUtility


class DBUtility(object):

    def __init__(self):
        self.creds = CredentialsUtility.get_db_credentials()
        self.db_port = self.creds['db_port'].pop()

    def create_connection(self):
        connection = pymysql.connect(host=self.creds['db_host'], user=self.creds['db_user'],
                                     password=self.creds['db_password'], port=self.db_port)

        return connection

    def execute_select(self, sql):
        connection = self.create_connection()

        try:
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql)
            response_dict = cursor.fetchall()
            cursor.close()
        except Exception as e:
            raise Exception(f"Failed running sql: {sql} \n Error: {str(e)}")
        finally:
            connection.close()

        return response_dict

    def execute_sql(self):
        pass
