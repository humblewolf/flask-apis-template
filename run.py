
import json
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask, jsonify, send_from_directory, request
from flask_restful import Api
from webargs.flaskparser import parser

from src.consts import sym
from src.middlewares.admin_middleware import FsAdminMiddleware
from src.routes import test_routes
from src.utils import gen_utils, sl_utils
from src.utils.external_services import mongodb_connector, gc_connector, redis_connector

############################################################
app = Flask(__name__, static_folder="static")

# 5 mb max upload limit
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024


@app.errorhandler(gen_utils.FmfException)
def handle_fmf_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = 200
    return response


@app.errorhandler(Exception)
def handle_exceptions_flask(e):
    codee = getattr(e, "code", 500)
    if codee == 405:
        response = jsonify("API route not found")
    else:
        gen_utils.log_current_traceback()
        response = jsonify("Something went wrong, we are looking into this, devs please check logs.")
    response.status_code = 200
    return response


# This error handler is necessary for webargs usage with Flask-RESTful
@parser.error_handler
def handle_error(err, req, schema, status_code, headers):
    raise gen_utils.FmfException(json.dumps(err.messages))


excp_handler = app.handle_exception
usr_excp_handler = app.handle_user_exception

mongodb_connector.init_app()
gc_connector.init_app()
redis_connector.init_app()
api = Api(app)

app.handle_exception = excp_handler
app.handle_user_exception = usr_excp_handler

# ----- routes here -------
# use new way of creating route files, see crud_boilerplate.py
api.add_resource(test_routes.Hello, '/hello')

#  --------routes end here ---------
# serve html pages from here
@app.route('/<path:path>')
def serve_page(path):
    return send_from_directory('static', path)


#  -------- log request and response -----------
@app.after_request
def superlog_response(resp):
    gen_utils.superlog_my_request_responses(request, resp)
    return resp


@app.before_request
def launch_middlewares():
    # here you can only run some code in various middlewares
    # return custom response or raise an exception or abort() in case you need to
    # otherwise let it go through
    FsAdminMiddleware().process_req()
    # MyAnotherMiddleware().process_req()


@app.before_first_request
def do_init_of_stack():
    sl_utils.write_superlog(origin=sym.SuperlogOrigins.wsgi_app.name, msg="Starting wsgi process, Performing init of stack, first build mongo indexes...")


handler = RotatingFileHandler('app.log', maxBytes=10000000, backupCount=3)
logger = logging.getLogger("fmf")
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)
app.logger = logger


# logger for periodic tasks
handler2 = RotatingFileHandler('periodic_tasks.log', maxBytes=10000000, backupCount=3)
logger2 = logging.getLogger("fmf_ptlog")
logger2.setLevel(logging.DEBUG)
logger2.addHandler(handler2)

# we are not using this way of inserting middlewares
# because in this way we are missing flask app settings,
# instead we are using flask's before_request
# app.wsgi_app = AdminMiddleware(app.wsgi_app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
