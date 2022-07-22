from .auth import auth_ns, user_ns
from .main import genres_ns, directors_ns, movies_ns

"""__all__ - это то, что можно будет тягать с помощью *
* обычно с лёта ставить не нужно, потому что можно сильно нагрузить кеш
лучше, если сначала пропишешь всё, что в неё хочешь сложить"""
__all__ = [
    'auth_ns',
    'user_ns',
    'genres_ns',
    'directors_ns',
    'movies_ns'
]
