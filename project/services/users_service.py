from typing import Optional

from project.dao import UsersDAO
from project.exceptions import ItemNotFound
from project.models import User
from project.tools.security import generate_tokens, approve_refresh_token, get_data_from_token, generate_password_hash


class UsersService:
    def __init__(self, dao: UsersDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> User:
        if user := self.dao.get_by_id(pk):  # Моржовый оператор проверяет значение
            # на истинность и если оно таково, записывает в переменную
            return user
        raise ItemNotFound(f'User with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> list[User]:
        return self.dao.get_all(page=page)

    def get_user_by_login(self, login):
        return self.dao.get_user_by_login(login)

    def create_user(self, login, password):
        self.dao.create(login, password)

    def check_user(self, login, password):
        """Положили в пользователя объект, который достали из базы по логину и пароль, полученный на вход"""
        user = self.get_user_by_login(login)
        return generate_tokens(email=user.email, password=password, password_hash=user.password)

    def update_token(self, refresh_token):
        return approve_refresh_token(refresh_token)

    def get_user_by_token(self, refresh_token):
        data = get_data_from_token(refresh_token)
        if data:
            return self.get_user_by_login(data.get('email'))

    def update_user(self, data, refresh_token):
        user = self.get_user_by_token(refresh_token)
        if user:
            self.dao.update_user(login=user.email, data=data)

    def update_password(self, data, refresh_token):
        user = self.get_user_by_token(refresh_token)
        if user:
            self.dao.update_user(login=user.email, data={'password': generate_password_hash(data.get('password_2'))})  # Уот??
            return self.check_user(login=user.email, password=data.get('password_2'))
