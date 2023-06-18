# -*- coding: utf-8 -*-
import uuid
import requests
import hashlib
import time

YOUDAO_URL = 'https://openapi.youdao.com/api'
APP_KEY = '6131dd361119cbbe'
APP_SECRET = 'Lecp90iqJtQTlJpFFWsuWvoIYPvkhLxq'

LANG = ['auto', 'zh-CHS', 'zh-CHT', 'en', 'ja', 'ko', 'fr', 'es', 'pt', 'it', 'ru', 'vi', 'de', 'ar']
'''
自动识别	auto 0
中文	zh-CHS 1
中文繁体	zh-CHT 2
英文	en 3
日文	ja 4
韩文	ko 5
法文	fr 6
西班牙文	es 7
葡萄牙文	pt 8
意大利文	it 9
俄文	ru 10
越南文	vi 11
德文	de 12
阿拉伯文	ar 13
'''

lang2index_dic = {
    "汉语": 1,
    "英语": 3,
    "西班牙语": 7,
    "法语": 6,
    "德语": 12,
    "意大利语": 9,
    "俄语": 10,
    "阿拉伯语": 13,
    "日语": 4,
    "韩语": 5,
    "葡萄牙语": 8,
    "中文繁体": 2,
    "越南语": 11
}


def encrypt(signStr):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(signStr.encode('utf-8'))
    return hash_algorithm.hexdigest()


def truncate(q):
    if q is None:
        return None
    size = len(q)
    return q if size <= 20 else q[0:10] + str(size) + q[size - 10:size]


def do_request(data):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    return requests.post(YOUDAO_URL, data=data, headers=headers).json()


class translation:
    def __init__(self, response):
        self.translated_text = response['translation']
        self.orgin_text = response['query']
        # self.translated_speak = response['tSpeakUrl']
        # self.orgin_speak = response[]


def translate(text, from_lang, to_lang):
    print('翻译(源语言' + from_lang + ')：' + text + '(' + to_lang + ')')
    data = {}
    data['from'] = from_lang
    data['to'] = to_lang
    data['signType'] = 'v3'
    curtime = str(int(time.time()))
    data['curtime'] = curtime
    salt = str(uuid.uuid1())
    signStr = APP_KEY + truncate(text) + salt + curtime + APP_SECRET
    sign = encrypt(signStr)
    data['appKey'] = APP_KEY
    data['q'] = text
    data['salt'] = salt
    data['sign'] = sign
    response = do_request(data)
    if response['errorCode'] == '102':
        return 1  # '不支持的语言类型'
    elif response['errorCode'] == '103':
        return 2  # '翻译文本过长'
    elif response['errorCode'] == '0':
        return translation(response)
    else:
        return False


if __name__ == '__main__':
    trans = translate("The text to be entered", LANG[0], LANG[1])
    # 返回类型有四种
    '''
    1#'不支持的语言类型'
    2#'翻译文本过长'
    translation:object#翻译成功
    False未知错误
    '''
    print(trans)
    print(trans.translated_text)
    print(trans.translated_text[0])
    print(trans.orgin_text)
    # 以下为上四句的输出
    '''
    <__main__.translation object at 0x7fc3e6ca5430>
    ['입력할 텍스트입니다']
    입력할 텍스트입니다
    The text to be entered
    '''

__all__ = ['translate', 'translation', 'LANG', 'lang2index_dic']
