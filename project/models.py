from sqlalchemy import Column, String, Integer

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'
    name = Column(String(100), unique=True, nullable=False)


class Director(models.Base):
    __tablename__ = 'directors'
    name = Column(String(100), unique=True, nullable=False)


class Movie(models.Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(String(255))
    trailer = """ссылка на трейлер"""
    year = Column(Integer)  # А они не стринги тоже?
    rating = Column(Integer)
    genre_id = Column(Integer)
    director_id = Column(Integer)


class User(models.Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    """не забывайте, что пароль тут будет в хешированном виде"""
    name = Column(String(255))
    surname = Column(String(255))
    favorite_genre = Column(String(255))