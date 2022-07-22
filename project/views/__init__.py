from .auth import auth_ns, user_ns
from .main import genres_ns, users_ns, directors_ns, movies_ns

__all__ = [
    'auth_ns',
    'genres_ns',
    'users_ns',
    'directors_ns',
    'movies_ns'
]
