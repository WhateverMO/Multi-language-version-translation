import redis
import json
import pickle
import pymysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,DATE, DATETIME,Integer, String, ForeignKey, UniqueConstraint, Index, Text,BOOLEAN
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine,and_
from timeit import default_timer

host = '43.138.162.174'
port_redis = 6379
db_redis_0 = 0
db_redis_1 = 1
# host = '120.48.66.93'
port_mysql = 3306
db_mysql = 'test_db'
User = 'root'
Password = 'shejidasai2022'
Charset='utf8'

pool = redis.ConnectionPool(host=host,port=port_redis,decode_responses=True,password=Password)
r0 = redis.StrictRedis(db=db_redis_0,connection_pool=pool)
r1 = redis.StrictRedis(db=db_redis_1,connection_pool=pool)

g_mysql_url = 'mysql+pymysql://%s:%s@%s:%d/%s?charset=%s' % (User, Password, host, port_mysql,db_mysql,Charset)
engine = create_engine(g_mysql_url)
Base = declarative_base()
# engine.execute('ALTER DATABASE '+db_mysql+' CHARSET=UTF8;')
Session = sessionmaker(bind=engine)

class UsingAlchemy(object):

    def __init__(self, commit=True, log_time=True, log_label=''):
        """

        :param commit: 是否在最后提交事务(设置为False的时候方便单元测试)
        :param log_time:  是否打印程序运行总时间
        :param log_label:  自定义log的文字
        """
        self._log_time = log_time
        self._commit = commit
        self._log_label = log_label+" -- 总用时"
        self._session = Session(bind=engine,expire_on_commit=False)

    def __enter__(self):

        # 如果需要记录时间
        if self._log_time is True:
            self._start = default_timer()

        return self

    def __exit__(self, *exc_info):
        # 提交事务
        if self._commit:
            self._session.commit()

        if self._log_time is True:
            diff = default_timer() - self._start
            print('-- %s: %.6f 秒' % (self._log_label, diff))

    @property
    def session(self):
        return self._session
