#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/15 下午10:06
# @Author  : Aries
# @Site    : 
# @File    : wx.py.py
# @Software: PyCharm Community Edition
from flask import Flask, request
from flask import Response
import json
import hashlib

wx_PORT = 80
app = Flask(__name__)


@app.route('/wx', methods=['GET'])
def wx_input():
    print('hello wx welcome')
    print(request.args.to_dict().get('signature'))
    signature = request.args.to_dict().get('signature')
    timestamp = request.args.to_dict().get('timestamp')
    nonce = request.args.to_dict().get('nonce')
    echostr = request.args.to_dict().get('echostr')
    if signature and timestamp and nonce and echostr:
        pass
    else:
        raise Exception('param not complete')
    with open('./config/login.json') as f:
        conf = json.loads(f.read().encode('utf-8', 'ignore'))
    token = conf['wx_platform_token']
    list = [token, timestamp, nonce]
    list.sort()
    sha1 = hashlib.sha1()
    map(sha1.update, list)
    hashcode = sha1.hexdigest()
    if hashcode == signature:
        return echostr
    else:
        return ""


@app.route('/test', methods=['GET'])
def test():
    timestamp = request.args.to_dict().get('timestamp')
    print(request.args.to_dict().get('sign'))
    return timestamp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=wx_PORT)
