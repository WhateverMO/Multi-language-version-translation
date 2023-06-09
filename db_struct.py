import datetime
import json

import pytz

from connection import *

book_lib_text = "booklib:"
book_lib_content_text = "booklibcontent:"


class useridpool(Base):
    __tablename__ = 'useridpool'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    is_lock = Column(BOOLEAN, default=False)


class authoridpool(Base):
    __tablename__ = 'authoridpool'
    author_id = Column(Integer, primary_key=True, autoincrement=True)
    is_lock = Column(BOOLEAN, default=False)


class rootbookidpool(Base):
    __tablename__ = 'rootbookidpool'
    b_id = Column(Integer, primary_key=True, autoincrement=True)


class bookidpool(Base):
    __tablename__ = 'bookidpool'
    b_id = Column(Integer, primary_key=True, autoincrement=True)


class users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(32), nullable=False)
    picture = Column(String(128), nullable=True)
    age = Column(Integer, nullable=True)
    gender = Column(String(8), nullable=True)
    phone_number = Column(String(16), nullable=True)
    email = Column(String(32), nullable=True)
    birthday = Column(DATE, nullable=True)
    area = Column(String(128), nullable=True)
    user_describe = Column(String(128), default=None)
    activate_time = Column(DATETIME, nullable=False)
    password = Column(String(64), nullable=False)
    following_count = Column(Integer, default=0)  # 关注数


class authores(Base):
    __tablename__ = 'authores'
    author_id = Column(Integer, primary_key=True)
    author_name = Column(String(32), nullable=False)
    author_describe = Column(String(128), default=None)
    picture = Column(String(64), nullable=True)
    age = Column(Integer, nullable=True)
    gender = Column(String(8), nullable=True)
    phone_number = Column(String(16), nullable=True)
    email = Column(String(128), nullable=True)
    birthday = Column(DATE, nullable=True)
    area = Column(String(64), nullable=True)
    password = Column(String(64), nullable=False)
    follower_count = Column(Integer, default=0)  # 粉丝数
    works_count = Column(Integer, default=0)  # 作品数


class bookclass(Base):
    __tablename__ = 'bookclass'
    bookclass_id = Column(Integer, primary_key=True, autoincrement=True)
    class_name = Column(String(32), nullable=False)


class languages(Base):
    __tablename__ = 'languages'
    lang_id = Column(Integer, primary_key=True, autoincrement=True)
    lang_name = Column(String(16), nullable=False)


class rootbooklib():
    def __init__(self, root_b_id, orgin_b_id, info):
        self.root_b_id = root_b_id
        self.orgin_b_id = orgin_b_id
        self.info = info
        pass

    def add2redis(self):
        r0.lpush(book_lib_text + str(self.root_b_id), self.root_b_id)
        r0.lpush(book_lib_text + str(self.root_b_id), self.orgin_b_id)
        r0.lpush(book_lib_text + str(self.root_b_id), json.dumps(self.info))


class booklib(Base):
    __tablename__ = 'booklib'
    b_id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey(authores.author_id))
    lang_id = Column(Integer, ForeignKey(languages.lang_id))
    bc_id = Column(Integer, ForeignKey(bookclass.bookclass_id))
    rootbookid = Column(Integer, nullable=False)
    name = Column(String(54), nullable=False)
    desc = Column(String(1024), default=None)
    cover_path = Column(String(64))
    create_time = Column(DATETIME, nullable=False, default=str(
        datetime.datetime.utcnow().replace(tzinfo=pytz.utc).astimezone(pytz.timezone("Asia/Shanghai"))))
    is_original = Column(String(64), nullable=False)


class user_barrage(Base):
    __tablename__ = 'user_barrage'
    user_id = Column(Integer, ForeignKey(users.user_id), primary_key=True)
    barrage = Column(String(1024))
    create_time = Column(DATETIME, nullable=False, default=str(
        datetime.datetime.utcnow().replace(tzinfo=pytz.utc).astimezone(pytz.timezone("Asia/Shanghai"))),
                         primary_key=True)


class user_books_barrage(Base):
    __tablename__ = 'user_books_barrage'
    user_id = Column(Integer, ForeignKey(users.user_id), primary_key=True)
    book_id = Column(Integer, ForeignKey(booklib.b_id), primary_key=True)
    barrage = Column(String(1024))
    create_time = Column(DATETIME, nullable=False, default=str(
        datetime.datetime.utcnow().replace(tzinfo=pytz.utc).astimezone(pytz.timezone("Asia/Shanghai"))),
                         primary_key=True)


class fan(Base):
    __tablename__ = 'fan'
    fan_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(users.user_id))
    author_id = Column(Integer, ForeignKey(authores.author_id))


if __name__ == '__main__':
    print("清除数据库并新建")
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    r0.flushdb()
