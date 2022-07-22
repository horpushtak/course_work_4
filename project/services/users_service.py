from typing import Optional
from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import User


class UsersService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> User:
        if user := self.dao.get_by_id(pk):  # Моржовый оператор проверяет значение
            # на истинность и если оно таково, записывает в переменную
            return user
        raise ItemNotFound(f'User with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> list[User]:
        return self.dao.get_all(page=page)