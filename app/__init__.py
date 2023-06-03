import os
from flask import Flask, request, jsonify, make_response
from Config import config_map
from flask_cors import *
from Database import *

# myhost = '192.168.67.142'  # 测试端口
myhost = '0.0.0.0'  # 本地端口
url_host = '43.138.162.174'


def create_app(config_name):
    """
    返回一个实例化并且配置好的app
    config_name: 选择环境的参数
    """
    app = Flask(__name__)
    # app.config['SESSION_COOKIE_PATH'] = '/'
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
            reco_book_dir = basedir + '/app/static/book_file/'
            reco_book_ids = os.listdir(reco_book_dir)
            new_reco_book_ids = []
            for id in reco_book_ids:
                if id not in ['1', '2', '3', '4', '5', '6']:
                    new_reco_book_ids.append(id)
            hot_book_ids = select_hot_book()[0]
            my_host = 'http://' + '43.138.162.174'
            lun_bos = my_host + "/static/lun_bo_file/"
            lun_path = basedir + '/app/static/lun_bo_file/'
            luns = []
            files = sorted(os.listdir(lun_path))
            for file in files:
                luns.append(lun_bos + file)
            books = []
            for b_id in new_reco_book_ids[:4]:
                if b_id not in hot_book_ids:
                    data = select_book(b_id)
                    book_name = data.get("name")
                    author_name = select_author(data.get("author_id")).get("author_name")
                    picture = data.get("cover_path")
                    book_desc = data.get("desc")
                    book = [b_id, book_name, author_name, book_desc, picture]
                    books.append(book)
            hot_books = []
            for b_id in hot_book_ids:
                data = select_book(b_id)
                book_name = data.get("name")
                author_name = select_author(data.get("author_id")).get("author_name")
                picture = data.get("cover_path")
                book_desc = data.get("desc")
                book_class = get_info_class(data.get("bc_id"))
                hot_books.append([b_id, book_name, author_name, book_desc, picture, book_class])
            return jsonify(books=books, lun=luns, hot_books=hot_books, code=200)

    # 注册蓝图
    from app import user
    from app import admin
    from app import author

    app.register_blueprint(user.user, url_prefix='/api/user')  # 用户蓝图
    app.register_blueprint(admin.admin, url_prefix='/api/admin')  # 管理员蓝图
    app.register_blueprint(author.author, url_prefix='/api/author')  # 作者蓝图
    return app
