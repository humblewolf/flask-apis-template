import logging

from src.utils import gen_utils

logger = logging.getLogger("fmf")


def write_superlog(uid="na", origin="", msg="", data_1="", data_2="", data_3=""):
    log = "SUPERLOG :: {} :: {} -- {} -- {} -- {} -- {} -- {}".format(gen_utils.timestamp_to_ist(gen_utils.get_unix_ts_millis()), uid, origin, msg, data_1, data_2, data_3)
    print(log)
    logger.info(log)
