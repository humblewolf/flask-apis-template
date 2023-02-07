import random
import string
import time
import uuid
from datetime import datetime
import pytz
import logging
import traceback
from time import strftime
from flask import request
from flask.wrappers import Response, Request
import jsons

from src.consts import sym
from src.utils import sl_utils

logger = logging.getLogger("fmf")


def non_unique_id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def generate_unique_id():
    return str(uuid.uuid4())


# int in python 3 is unbound (limits only by machine hardware (word size), which is quite big)
# dont worry about y2038 problem
# https://stackoverflow.com/a/7604981/5457916
# mongo also stores very long integers without any issues (max be like 9223372036854775807),
# which if assumed timestamp in millis will be several thousand years into future
# bottomline is :: timestamp in secs and millis is safe to deal with and wont get into overflow problems in our stack
def get_unix_ts_seconds():
    return int(time.time())


# int in python 3 is unbound (limits only by machine hardware (word size), which is quite big)
# dont worry about y2038 problem
# https://stackoverflow.com/a/7604981/5457916
# mongo also stores very long integers without any issues (max be like 9223372036854775807),
# which if assumed timestamp in millis will be several thousand years into future
# bottomline is :: timestamp in secs and millis is safe to deal with and wont get into overflow problems in our stack
def get_unix_ts_millis():
    return int(round(time.time() * 1000))


def timestamp_to_ist(timestampMillis):
    try:
        tz = pytz.timezone('Asia/Kolkata')
        return datetime.fromtimestamp(timestampMillis/1000, tz).strftime('%d-%m-%Y %H:%M:%S')
    except:
        return None


class FmfException(Exception):

    def __init__(self, message):
        Exception.__init__(self)
        self.message = message

    def to_dict(self):
        return {"err_msg": self.message, "time": timestamp_to_ist(get_unix_ts_millis())}


def log_current_traceback():
    """ Logging after every Exception. """
    ts = strftime('[%Y-%b-%d %H:%M]')
    tb = traceback.format_exc()
    logger.error('%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s',
                 ts,
                 request.remote_addr,
                 request.method,
                 request.scheme,
                 request.full_path,
                 tb)


def superlog_my_request_responses(req: Request, resp: Response):

    try:
        if req.method == sym.RequestMethod.POST.name and (req.content_length is None or req.content_length < 100000):
            request_data = req.values.to_dict(flat=True)
            if req.content_type == "application/json":
                request_data.update(jsons.loads(req.data.decode('utf-8')))
        elif req.method == sym.RequestMethod.POST.name:
            request_data = "post request data too long"
        elif req.method == sym.RequestMethod.GET.name:
            request_data = req.values.to_dict(flat=True)
        else:
            request_data = "unknown http method"
    except Exception as ex:
        request_data = "some exception occurred while capturing request data - {}".format(ex)

    try:
        if resp.content_length is None or resp.content_length < 100000:
            response_data = resp.get_data(as_text=True)
        else:
            response_data = "response too long"
    except Exception as ex:
        response_data = "some exception occurred while capturing response data - {}".format(ex)

    sl_utils.write_superlog(origin=sym.SuperlogOrigins.flask_api_logger.name, msg=req.path, data_1=request_data, data_2=response_data, data_3=req.method)