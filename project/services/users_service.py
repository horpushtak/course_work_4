from typing import Optional

from flask import request

from project.dao import UsersDAO
from project.exceptions import ItemNotFound
from project.models import User
from project.tools.security import generate_tokens


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
        return generate_tokens(user=self.get_user_by_login(login), password=password)
