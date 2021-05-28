from .base import *
import environ

env = environ.Env()
# Open .env file
environ.Env.read_env()


# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env("SECRET_KEY")


DEBUG = False

ALLOWED_HOSTS = [
    'http://allowed.site',
]

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8081',
)
