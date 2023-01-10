import os

from flask import Flask, request, jsonify, make_response
from Config import config_map
from flask_cors import *
from Database import *


def create_app(config_name):
    """
    返回一个实例化并且配置好的app
    config_name: 选择环境的参数
    """
    app = Flask(__name__)
    # CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)

    # 这里需要实例化数据库

    # Session(app)  # 利用flask_session,将session数据保存到redis中
    app.secret_key = "12fa12f13f1fbb589wh4"
    CORS(app)

    @app.after_request
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

    # 游客首页
    @app.route('/api', methods=['GET', 'POST'])
    def index():
        if request.method == 'GET':
            basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
            hot_book_dir = basedir + '/app/static/reco_book/'
            book_ids = os.listdir(hot_book_dir)
            books = []
            for b_id in book_ids:
                book_name = select_book(b_id).get("name")
                # lang_id = select_book(b_id).get("lang_id")
                author_name = select_author(select_book(b_id).get("author_id")).get("author_name")
                picture = select_book(b_id).get("cover_path")
                book_desc = select_book(b_id).get("desc")
                book = [b_id, book_name, author_name, book_desc, picture]
                books.append(book)
            return jsonify(books=books, code=200)

    # 注册蓝图
    from app import user
    from app import admin
    from app import author

    app.register_blueprint(user.user, url_prefix='/api/user')  # 用户蓝图
    app.register_blueprint(admin.admin, url_prefix='/api/admin')  # 管理员蓝图
    app.register_blueprint(author.author, url_prefix='/api/author')  # 作者蓝图
    return app
