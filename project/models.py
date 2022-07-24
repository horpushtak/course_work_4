from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'
    name = Column(String(100), unique=True, nullable=False)


class Director(models.Base):
    __tablename__ = 'directors'
    name = Column(String(100), unique=True, nullable=False)


class Movie(models.Base):
    __tablename__ = 'movies'
    title = Column(String(255), nullable=False, unique=True)
    description = Column(String(255))
    trailer = Column(String(255))  # Тут юрла лежит
    year = Column(Integer)
    rating = Column(Float())
    genre_id = Column(Integer, ForeignKey(f'{Genre.__tablename__}.id'))
    # Вытянет название таблицы (каким бы оно ни стало в итоге) и id
    director_id = Column(Integer, ForeignKey(f'{Director.__tablename__}.id'))
    genre = relationship('Genre')
    director = relationship('Director')


class User(models.Base):
    __tablename__ = 'users'
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255))
    """не забывайте, что пароль тут будет в хешированном виде"""  # Имеется в виду, что будет строка?
    name = Column(String(255))
    surname = Column(String(255))
    favourite_genre = Column(Integer, ForeignKey(f'{Genre.__tablename__}.id'))
    genre = relationship('Genre')
