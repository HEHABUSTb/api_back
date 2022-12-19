import logging
import random
import string


def generate_random_email_and_password(domain=None, email_prefix=None):
    logging.info('Generate random email and password')

    if not domain:
        domain = 'gmail.com'

    if not email_prefix:
        email_prefix = 'test_user'

    random_email_string_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))
    email = email_prefix + '_' + random_string + '@' + domain

    password_lenght = 10
    password = ''.join(random.choices(string.ascii_lowercase, k=password_lenght))

    random_info = {'email': email, 'password': password}
    logging.info(f'Randomly generated email and password: {random_info}')

    return random_info
