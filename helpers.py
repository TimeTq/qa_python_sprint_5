import random
from string import ascii_lowercase, ascii_uppercase, digits


ALPHABET = ascii_uppercase + ascii_lowercase + digits
LENGTH = 8


def get_user_name():
    return ''.join(random.choices(ALPHABET, k=LENGTH))


def get_user_login():
    login = ''.join(random.choices(ALPHABET, k=LENGTH))
    domain = 'ya'
    return f'{login}@{domain}.ru'


def get_user_password():
    return ''.join(random.choices(ALPHABET, k=LENGTH))
