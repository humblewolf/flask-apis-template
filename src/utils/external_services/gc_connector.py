# import atexit
# from google.cloud import logging as gclg
#
#
# # not creating connection/client per request,
# # instead reusing old connection/client
# # ISSUE:
# # 1. what is the consequences of dangling connections on server side because here worker might end abruptly ?
# # 2. is celery main process gracefully terminating worker processes, because we dont get it in logs after ctrl-c ?
# gcl_preserved = None
#
#
# def create_gcl_preserved():
#     global gcl_preserved
#     print("[GCL] **** gcl client getting created and will be preserved ****")
#     gcl_preserved = gclg.Client.from_service_account_json('thevirtapp-gcp-cld-logging-key.json')
#
#
# def get_gcl_by_reuse():
#     global gcl_preserved
#     if gcl_preserved is None:
#         print("[GCL] ** old gcl client not found, thus creating new **")
#         create_gcl_preserved()
#
#     print("[GCl] preserved GCL client ready to serve")
#     return gcl_preserved
#
#
# def close_preserved_gcl():
#     global gcl_preserved
#     print("[GCl] * trying to close preserved gcl client * ")
#     if gcl_preserved is not None:
#         print("[GCl] * calling close on preserved gcl client * ")
#         gcl_preserved.close()
#
#
# def init_app():
#     atexit.register(close_preserved_gcl)


def init_app():
    pass
