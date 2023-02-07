# import logging
# import atexit
#
# from pymongo import MongoClient as mc
#
# from fyndster.consts import config
#
#
# # https://flask-pymongo.readthedocs.io/en/latest/index.html
# # https://stackoverflow.com/a/41655413/5457916
# # ----
# # not creating connection/client per request,
# # instead reusing old connection/client
# # ISSUE:
# # 1. what is the consequences of dangling connections on server side because here worker might end abruptly ?
# # 2. is celery main process gracefully terminating worker processes, because we dont get it in logs after ctrl-c ?
# logger = logging.getLogger("fmf")
# dbcl_preserved = None
#
#
# def create_dbcl_preserved():
#     global dbcl_preserved
#     print("[MONGO] **** mongodb connection getting created and will be preserved, with pool size of 400 ****")
#     dbcl_preserved = mc(config.mongo_uri, maxPoolSize=400)
#
#
# def get_db_client_by_reuse():
#     global dbcl_preserved
#     if dbcl_preserved is None:
#         print("[MONGO] ** old preserved mongo connection not found, thus creating new **")
#         create_dbcl_preserved()
#
#     print("[MONGO] preserved mongo connection ready to serve")
#     return dbcl_preserved
#
#
# def get_db():
#     return get_db_client_by_reuse()[config.main_db_name]
#
#
# def get_collection(coll_name=None):
#     if coll_name is not None:
#         return get_db()[coll_name]
#     else:
#         return None
#
#
# def close_preserved_dbcl():
#     global dbcl_preserved
#     print("[MONGO] * trying to close preserved mongo connection * ")
#     if dbcl_preserved is not None:
#         print("[MONGO] * calling close on preserved mongo connection * ")
#         dbcl_preserved.close()
#
#
# def init_app():
#     atexit.register(close_preserved_dbcl)


def init_app():
    pass