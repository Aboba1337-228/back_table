import pymysql
from configs.config_db import settings

connect = pymysql.connect(
    settings['host'], 
    settings['user'], 
    settings['password'], 
    settings['db']
)