import logging

from flask import g
from flask_restful import Resource
from webargs.flaskparser import use_args

from src.args import gen_args

logger = logging.getLogger("fmf")


class Hello(Resource):
    @use_args(gen_args.argsTest)
    def get(self, args):
        return f'hello from humblewolf and {args["name"]}'
