import hashlib
import time
import simplejson as json


def result(code=200, d={}):
    data = dict()  # object.__dict__
    data['code'] = code
    data['data'] = d
    return json.dumps(data, ensure_ascii=False)


def md5(m):
    return hashlib.md5(m.encode()).hexdigest()


def getNowDataTime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def getTimeStamp():
    return time.time()


def getOrderNum():
    orderNum = str(getTimeStamp()).replace('.', '')
    return orderNum
