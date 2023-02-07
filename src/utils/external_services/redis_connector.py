# import redis
# import redisearch
# import atexit
#
# from fyndster.consts import config
#
#
# # https://stackoverflow.com/questions/49398590/correct-way-of-using-redis-connection-pool-in-python
# # ---
# # not creating connection/client per request,
# # instead reusing old connection/client
# # ISSUE:
# # 1. what is the consequences of dangling connections on server side because here worker might end abruptly ?
# # 2. is celery main process gracefully terminating worker processes, because we dont get it in logs after ctrl-c ?
# redis_preserved = None
#
#
# def create_redis_preserved(db_index=0):
#     global redis_preserved
#     print("[REDIS] **** redis client getting created and will be preserved ****")
#     redis_preserved = redis.Redis(db=db_index).from_url(config.redis_uri)
#
#
# def get_redis_instance(db_index=0):
#     global redis_preserved
#     if redis_preserved is None:
#         print("[REDIS] ** old redis client not found, thus creating new **")
#         create_redis_preserved(db_index)
#
#     print("[REDIS] preserved redis client ready to serve")
#     return redis_preserved
#
#
# def get_redisearch_client(index_name):
#     # return redisearch.Client(index_name, host=config.redisearch_host, port=config.redisearch_port)
#     return redisearch.Client(index_name, conn=get_redis_instance())
#
#
# def close_preserved_gcl():
#     global redis_preserved
#     print("[REDIS] * trying to close preserved redis client * ")
#     if redis_preserved is not None:
#         print("[REDIS] * calling close on preserved redis client * ")
#         redis_preserved.close()
#
#
# def init_app():
#     atexit.register(close_preserved_gcl)


def init_app():
    pass
