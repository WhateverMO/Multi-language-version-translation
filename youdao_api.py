# -*- coding: utf-8 -*-
import json
import requests
import hashlib
import time
import uuid

# 您的应用ID
APP_KEY = ''
# 您的应用密钥
APP_SECRET = ''
APP_KEY = '6131dd361119cbbe'
APP_SECRET = 'Lecp90iqJtQTlJpFFWsuWvoIYPvkhLxq'

LANG = ['auto','zh-CHS','zh-CHT','en','ja','ko','fr','es','pt','it','ru','vi','de','ar']

'''
添加鉴权相关参数 -
    appKey : 应用ID
    salt : 随机值
    curtime : 当前时间戳(秒)
    signType : 签名版本
    sign : 请求签名

    @param appKey    您的应用ID
    @param appSecret 您的应用密钥
    @param paramsMap 请求参数表
'''


def addAuthParams(appKey, appSecret, params):
    q = params.get('q')
    if q is None:
        q = params.get('img')
    salt = str(uuid.uuid1())
    curtime = str(int(time.time()))
    sign = calculateSign(appKey, appSecret, q, salt, curtime)
    params['appKey'] = appKey
    params['salt'] = salt
    params['curtime'] = curtime
    params['signType'] = 'v3'
    params['sign'] = sign


'''
    计算鉴权签名 -
    计算方式 : sign = sha256(appKey + input(q) + salt + curtime + appSecret)
    @param appKey    您的应用ID
    @param appSecret 您的应用密钥
    @param q         请求内容
    @param salt      随机值
    @param curtime   当前时间戳(秒)
    @return 鉴权签名sign
'''


def calculateSign(appKey, appSecret, q, salt, curtime):
    strSrc = appKey + getInput(q) + salt + curtime + appSecret
    return encrypt(strSrc)


def encrypt(strSrc):
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(strSrc.encode('utf-8'))
    return hash_algorithm.hexdigest()


def getInput(input):
    if input is None:
        return input
    inputLen = len(input)
    return input if inputLen <= 20 else input[0:10] + str(inputLen) + input[inputLen - 10:inputLen]


def createRequest(text,from_lang,to_lang):
    '''
    note: 将下列变量替换为需要请求的参数
    '''
    q = text
    lang_from = from_lang
    lang_to = to_lang

    data = {'q': q, 'from': lang_from, 'to': lang_to}

    addAuthParams(APP_KEY, APP_SECRET, data)

    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    res = requests.post('https://openapi.youdao.com/api',data, header)
    res = str(res.content, 'utf-8')
    res = json.loads(res)
    return res

class translation:
    def __init__(self,response):
        self.translated_text = response['translation']
        self.orgin_text = response['query']
        # self.translated_speak = response['tSpeakUrl']
        # self.orgin_speak = response[]

def translate(text,from_lang,to_lang):
    print('翻译(源语言'+from_lang+')：'+text+'('+to_lang+')')
    response = createRequest(text,from_lang,to_lang)
    if response['errorCode'] == '102':
        return 1#'不支持的语言类型'
    elif response['errorCode'] == '103':
        return 2#'翻译文本过长'
    elif response['errorCode'] == '0':
        return translation(response)
    else: return False


if __name__ == '__main__':
    trans = translate("The text to be entered",LANG[3],LANG[5])
    #返回类型有四种
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
    #以下为上四句的输出
    '''
    <__main__.translation object at 0x7fc3e6ca5430>
    ['입력할 텍스트입니다']
    입력할 텍스트입니다
    The text to be entered
    '''

__all__ = ['translate','translation','LANG']