from enum import Enum


class RequestMethod(Enum):
    GET = 1
    POST = 2


class SuperlogOrigins(Enum):
    flask_api_logger = 1
    wsgi_app = 2
