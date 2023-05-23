import random
from flask import request, jsonify, session, g, make_response, render_template, url_for, redirect
from . import admin
from ..utils.tool import user_login_required
import os
from datetime import datetime
from werkzeug.utils import secure_filename
from Database import *


@admin.after_request
def func_res(resp):
    res = make_response(resp)
    res.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    res.headers['Access-Control-Allow-Methods'] = 'GET,POST,DELETE,PUT,OPTIONS'
    res.headers[
        'Access-Control-Allow-Headers'] = 'X-Requested-With,Content-Type, Content-Length, Authorization, Accept, yourHeaderFeild'
    res.headers['Access-Control-Allow-Credentials'] = 'true'
    res.headers['X-Powered-By'] = '3.2.1'
    res.headers['Content-Type'] = 'application/json;charset=utf-8'
    return res


@admin.route('/addHotbook', methods=['GET,POST'])
def addHotbook():
    if request.method == 'POST':
        b_id = request.form.get("book_id")
        b_id_list = [b_id]
        try:
            set_hot_book(b_id_list)
        except Exception as e:
            print(e)
            return jsonify(msg="热门图书添加失败", code=4000)
        return jsonify(msg='热门图书添加成功', code=200)
