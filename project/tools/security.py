import base64
import hashlib

import calendar
import datetime
from os import abort

import jwt
from flask import current_app



def __generate_password_digest(password: str) -> bytes:
    return hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=current_app.config["PWD_HASH_SALT"],
        iterations=current_app.config["PWD_HASH_ITERATIONS"],
    )


def generate_password_hash(password: str) -> str:
    return base64.b64encode(__generate_password_digest(password)).decode('utf-8')


# TODO: [security] Описать функцию compose_passwords(password_hash: Union[str, bytes], password: str)

def compare_passwords_hash(password_hash, comparing_password):
    return password_hash == generate_password_hash(comparing_password)  # Сохранённый в базе хэш нужно сравнить с паролем,
    # который передал пользователь и его мы тоже приводим к хэшу


def generate_tokens(email, password, password_hash=None, is_refresh=False):

    if not email:
        abort()
    """Так, я подзабыл как именно работает вот это присваивание в аргуметах функции compare_passwords_hash
    сначала пишется имя переменной, как она описана в используемой функции, а приравневается та переменная, чтоб
    используется здесь, в generate_tokens"""
    if not is_refresh:
        if not compare_passwords_hash(comparing_password=password, password_hash=password_hash):
            abort()

    data = {
        "username": email,
        "password": password
        }

    min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=current_app.config['TOKEN_EXPIRE_MINUTES'])
    data['exp'] = calendar.timegm(min30.timetuple())
    asses_token = jwt.encode(data, key=current_app.config['SECRET_KEY'], algorithm=current_app.config['ALGORITHM'])

    day30 = datetime.datetime.utcnow() + datetime.timedelta(days=current_app.config['TOKEN_EXPIRE_DAYS'])
    data['exp'] = calendar.timegm(day30.timetuple())
    refresh_token = jwt.encode(data, key=current_app.config['SECRET_KEY'], algorithm=current_app.config['ALGORITHM'])

    return {'asses_token': asses_token, 'refresh_token': refresh_token}


def approve_refresh_token(refresh_token):
    data = jwt.decode(jwt=refresh_token, key=current_app.config['SECRET_KEY'], algorithm=current_app.config['ALGORITHM'])
    email = data.get('email')
    password = data.get('password')

    return generate_tokens(email, password, is_refresh=True)
