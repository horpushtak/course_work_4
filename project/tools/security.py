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

def compare_passwords_hash(password_hash, password):
    return password_hash == generate_password_hash(password)  # Сохранённый в базе хэш нужно сравнить с паролем,
    # который передал пользователь и его мы тоже приводим к хэшу


def generate_tokens(user, password, is_refresh=False):

    if not user:
        abort(404)

    if not is_refresh:
        if not compare_passwords_hash(password, user.password):
            abort(404)

    data = {
        "username": user.email,
        "password": user.password
        }

    min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=current_app.config['TOKEN_EXPIRE_MINUTES'])
    data['exp'] = calendar.timegm(min30.timetuple())
    asses_token = jwt.encode(data, key=current_app.config['SECRET_KEY'], algoritm=current_app.config['ALGORITHM'])

    day30 = datetime.datetime.utcnow() + datetime.timedelta(days=current_app.config['TOKEN_EXPIRE_DAYS'])
    data['exp'] = calendar.timegm(day30.timetuple())
    refresh_token = jwt.encode(data, key=current_app.config['SECRET_KEY'], algoritm=current_app.config['ALGORITHM'])

    return {'asses_token': asses_token, 'refresh_token': refresh_token}
