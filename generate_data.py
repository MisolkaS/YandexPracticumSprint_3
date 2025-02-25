import random
import string
def generate_random_user_data(name_length=6, email_length=8, password_length=6, domain='random.ru'):
    name = ''.join(random.choices(string.ascii_letters, k=name_length))
    email_prefix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=email_length))
    email = f"{email_prefix}@{domain}"
    password = ''.join(random.choices(string.ascii_letters, k=password_length))

    return {
        'name': name,
        'email': email,
        'password': password
    }