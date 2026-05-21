import random
import string
from faker import Faker

fake = Faker('ru_RU')

def generate_random_phone():
    """Генерация случайного номера телефона"""
    return f"+7999{random.randint(1000000, 9999999)}"

def generate_random_email():
    """Генерация случайного email"""
    return fake.email()

def generate_random_password(length=10):
    """Генерация валидного пароля (заглавная + строчные + цифры)"""
    uppercase = random.choice(string.ascii_uppercase)
    lowercase = ''.join(random.choices(string.ascii_lowercase, k=length-3))
    digits = ''.join(random.choices(string.digits, k=2))
    password = uppercase + lowercase + digits
    return ''.join(random.sample(password, len(password)))

def generate_invalid_password():
    """Генерация невалидного пароля (только цифры)"""
    return ''.join(random.choices(string.digits, k=8))

def generate_random_name():
    """Генерация случайного имени (кириллица)"""
    return fake.first_name()

def generate_random_last_name():
    """Генерация случайной фамилии (кириллица)"""
    return fake.last_name()