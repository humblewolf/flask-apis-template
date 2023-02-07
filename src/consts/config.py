import os

# this can be one of 'dev', 'stg' and 'prod', shall default to dev....
project_realm = os.getenv('WEBAPIS_REALM', 'dev')
webapis_version = 1.0
main_db_name = "my_db"
mongo_uri = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')