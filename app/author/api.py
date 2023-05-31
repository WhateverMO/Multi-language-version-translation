import random
from flask import request, jsonify, session, g, make_response, render_template, url_for, redirect
from . import author
from ..utils.tool import user_login_required, author_login_required
import os
from datetime import datetime
from werkzeug.utils import secure_filename
from Database import *
from app import myhost


@author.after_request
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


# 译者注册界面
@author.route('/register', methods=['POST'])
def author_register():
    if request.method == 'POST':
        data = request.form
        author_name = data.get("author_name")
        password = data.get("password")
        password2 = data.get("password2")
        # 校验参数
        if not all([author_name, password, password2]):
            return jsonify(msg="参数不完整", code=4002)

        if password != password2:
            return jsonify(msg="两次密码不一致", code=4001)
        my_host = "http://" + myhost + ":5000"
        avatar = my_host + "/static/avatar_file/b2.jpg"
        author_id = add_author(authores(author_name=author_name, password=password, picture=avatar))
        # 保存登陆状态到session中
        session["author_name"] = author_name
        session["author_id"] = author_id
        session["author_avatar"] = avatar
        # 返回结果
        return jsonify(msg="注册成功", author_id=author_id, code=200)


# 译者登录接口
@author.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.form
        author_id = data.get("author_id")
        password = data.get('password')
        if not all([author_id, password]):
            return jsonify(msg='缺少参数', code=4000)
        else:
            if login_author(author_id, password) == -1:
                return jsonify(msg="账号或密码错误", code=4002)
            elif login_author(author_id, password):
                # 如果验证通过保持登录状态在session中
                session["author_id"] = author_id
                author_name = select_author(author_id).get("author_name")
                session["author_name"] = author_name
                return jsonify(msg="登陆成功", code=200)
            else:
                return jsonify(msg='账号或密码错误', code=4000)


# 检查登录状态
@author.route('/session', methods=['GET'])
def check_session():
    author_id = session.get("author_id")
    author_name = session.get("author_name")
    author_describe = session.get("author_describe")
    author_picture = session.get("author_avatar")
    author_age = session.get("author_age")
    author_gender = session.get("author_gender")
    author_phone_number = session.get("author_phone_number")
    author_email = session.get("author_email")
    author_birthday = session.get("author_birthday")
    author_area = session.get("author_area")
    if author_id is not None:
        return jsonify(author_id=author_id, author_name=author_name, author_describe=author_describe,
                       author_picture=author_picture, author_age=author_age, author_gender=author_gender,
                       author_phone_number=author_phone_number,
                       author_email=author_email, author_birthday=author_birthday, author_area=author_area, code=200)
    else:
        return jsonify(msg='未登录', code=4000)


# 退出登录
@author.route('/logout', methods=['DELETE'])
@author_login_required  # 验证作者登录的装饰器
def logout():
    if request.method == 'DELETE':
        session.clear()
        return jsonify(msg="成功退出登录", code=200)


# 修改密码
@author.route('/checkpassword', methods=['POST'])
@author_login_required  # 验证用户登录装的饰器
def change_password():
    if request.method == 'POST':
        aid = g.author_id
        data = request.form
        password = data.get("password")
        new_password = data.get("new_password")
        # 校验参数完整
        if not all([new_password, password, aid]):
            return jsonify(msg="参数不完整", code=4000)
        if select_author(aid) == -1:
            return jsonify(msg="获取作者信息失败", code=4000)
        # 用数据库里的密码与用户输入的密码进行对比验证
        if not login_author(aid, password):
            return jsonify(msg='原始密码错误', code=4000)
        # 修改密码
        update_author(aid, {"password": new_password})
        return jsonify(msg='修改密码成功', code=200)


# 作者查看基本信息
@author.route('/information', methods=['GET'])
@author_login_required  # 验证用户登录的装饰器
def get_author_information():
    if request.method == 'GET':
        # 从管道获取author的id
        author_id = g.author_id
        data = select_author(author_id)
        if data == -1:
            return jsonify(msg="该作者不存在", code=4002)
        else:
            author_name = data.get("author_name")
            author_age = data.get("age")
            author_gender = data.get("gender")
            author_area = data.get("area")
            author_describe = data.get("author_describe")
            author_phone_number = data.get("phone_number")
            author_email = data.get("email")
            author_birthday = data.get("birthday")
            author_avatar = data.get("picture")
            return jsonify(author_name=author_name, author_id=author_id, author_age=author_age,
                           author_gender=author_gender,
                           author_area=author_area,
                           author_describe=author_describe, author_phone_number=author_phone_number,
                           author_email=author_email,
                           author_birthday=author_birthday, author_avatar=author_avatar, code=200)


# 作者修改基本信息
@author.route('/information/modification', methods=['POST'])
@author_login_required  # 验证用户登录的装饰器
def update_author_information():
    if request.method == 'POST':
        # 从管道获取user的id
        author_id = g.author_id
        # 获取用户修改的信息
        data = request.form
        author_name = data.get("author_name")
        author_age = data.get("author_age")
        author_gender = data.get("author_gender")
        author_area = data.get("author_area")
        author_describe = data.get("author_describe")
        author_phone_number = data.get("author_phone_number")
        author_email = data.get("author_email")
        author_birthday = data.get("author_birthday")
        try:
            update_author(author_id,
                          {"author_name": author_name, "age": author_age, "gender": author_gender,
                           "area": author_area,
                           "author_describe": author_describe,
                           "phone_number": author_phone_number, "email": author_email,
                           "birthday": author_birthday})
        except Exception as e:
            print(e)
            return jsonify(msg="保存失败，请重新检查输入的信息是否合法", code=4000)
        # 保存成功并返回
        session["author_name"] = author_name
        session["author_age"] = author_age
        session["author_gender"] = author_gender
        session["author_area"] = author_area
        session["author_describe"] = author_describe
        session["author_phone_number"] = author_phone_number
        session["author_email"] = author_email
        session["author_birthday"] = author_birthday
        return jsonify(msg="保存成功", author_name=author_name, author_id=author_id, author_age=author_age,
                       author_gender=author_gender,
                       author_area=author_area,
                       author_describe=author_describe, author_phone_number=author_phone_number,
                       author_email=author_email,
                       author_birthday=author_birthday, code=200)


# 作者修改头像
@author.route('/information/modification/update_avatar', methods=['POST', 'GET'])
@author_login_required
def update_user_avatar():
    if request.method == 'POST':
        author_id = g.author_id
        # 获取用户上传的头像图片文件
        image_file = request.files.get("file")
        # 获取安全的文件名
        filename = secure_filename(image_file.filename)
        # 获取上上级路径
        basedir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        # 文件重命名
        filename = "author_" + str(author_id) + "." + \
                   filename.rsplit('.', 1)[1]
        file_path = basedir + "/app/static/avatar_file/" + filename
        if image_file is None:
            return jsonify(msg="未上传图片", code=4000)
        try:
            image_file.save(file_path)
            my_host = "http://" + myhost + ":5000"
            avatar_url = my_host + "/static/avatar_file/" + filename
        except Exception as e:
            print(e)
            return jsonify(msg="上传图片失败", code=4001)
        session["picture"] = avatar_url
        update_author(author_id, {"picture": avatar_url})
        return jsonify(msg="修改头像成功", user_avatar=avatar_url, code=200)


# 作者添加书籍选项页面
@author.route('/add_books_index', methods=['POST', 'GET'])
@author_login_required
def author_add_books_index():
    if request.method == 'POST':
        try:
            author_id = g.author_id
            name = request.form.get("name")
            lang_id = request.form.get("lang_id")
            bc_id = request.form.get("bc_id")
            book_desc = request.form.get("book_desc")
            my_host = "http://" + myhost + ":5000"
            picture = my_host + "/static/cover_file/b1.jpg"
            book_id = add_book(
                booklib(author_id=author_id, name=name, lang_id=lang_id, bc_id=bc_id, desc=book_desc,
                        cover_path=picture))
        except Exception as e:
            print(e)
            return jsonify(msg="建立新书失败请重试", code=4000)
        return jsonify(msg="建立新书成功", code=200, book_id=book_id, author_id=author_id, lang_id=lang_id)


# 作者添加书籍(只能是原始语言)
@author.route('/addbooks/<int:book_id>/<int:c_no>', methods=['GET', 'POST'])
@author_login_required
def add_books(book_id, c_no):
    if request.method == 'POST':
        content = str(request.form.get("content"))
        title = str(request.form.get('title'))
        if add_content(book_id, c_no, title, content):
            return jsonify(msg="提交成功", code=200)
        else:
            return jsonify(msg="提交失败，请重试", code=4000)


# 作者查看自己的书籍
@author.route('/get_my_books', methods=['GET'])
@author_login_required
def get_my_books():
    if request.method == 'GET':
        author_id = g.author_id
        datas = select_this_author_s_all_book(author_id)
        books = []
        if datas:
            for data in datas:
                books.append({'book_id': data.get('b_id'), 'book_name': data.get('name'),
                              'desc': data.get('desc'), 'cover_path': data.get('cover_path')})
            return jsonify(msg='查询到该作者的书籍', books=books, code=200)
        else:
            return jsonify(msg='该作者没有书籍', code=4000)


# 查看自己的书籍具体章节信息
@author.route('/get_my_books/<int:book_id>/<int:c_no>', methods=['GET'])
@author_login_required
def book_detail(book_id, c_no):
    title = select_bookcontent(book_id, c_no)[0]
    content_text = select_bookcontent(book_id, c_no)[1]
    return jsonify(content_text=content_text, title=title)


# 作者修改章节内容
@author.route('/edit_my_books/<int:book_id>/<int:c_no>', methods=['GET', 'POST'])
@author_login_required
def edit_books_center(book_id, c_no):
    if request.method == 'GET':
        title = select_bookcontent(book_id, c_no)[0]
        content_text = select_bookcontent(book_id, c_no)[1]
        return jsonify(content_text=content_text, title=title)
    if request.method == 'POST':
        content = str(request.form.get("content"))
        title = str(request.form.get('title'))
        if add_content(book_id, c_no, title, content):
            return jsonify(msg="提交成功", code=200)
        else:
            return jsonify(msg="提交失败，请重试", code=4000)


# 上传书籍封面
@author.route('/add_books_cover/<int:book_id>', methods=['POST'])
@author_login_required
def add_book_picture(book_id):
    cover_file = request.files.get("file")
    filename = secure_filename(cover_file.filename)
    basedir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    filename = str(book_id) + "." + filename.rsplit('.', 1)[1]
    file_path = basedir + "/app/static/cover_file/" + filename
    if cover_file is None:
        return jsonify(msg="未上传图片", code=4000)
    try:
        cover_file.save(file_path)
        my_host = "http://" + myhost + ":5000"
        cover_url = my_host + "/static/cover_file/" + filename
    except Exception as e:
        print(e)
        return jsonify(msg="上传图片失败", code=4001)
    update_book(book_id, {"cover_path": cover_url})
    return jsonify(msg="上传封面成功", book_picture=cover_url, code=200)


# 搜索
@author.route('/book/search/<string:book_name>', methods=['GET'])
def book_search(book_name):
    res = search_book(book_name)
    if not res:
        return jsonify(msg='没有找到任何有关书籍', code=4000)
    else:
        return jsonify(msg='找到有关书籍', books=res, code=200)


# 查看书籍的其他译本
@author.route('/other/<int:book_id>', methods=['GET'])
def get_other_book(book_id):
    data = select_all_edition_b_id_by_b_id(book_id)
    datas = list(set(data))
    books = []
    if data != -1:
        for b_id in datas:
            books.append(select_book(b_id))
    return jsonify(books=books)


# 译者翻译选项界面
@author.route('/translate_option/<int:book_id>', methods=['GET', 'POST'])
@author_login_required
def translate_option(book_id):
    if request.method == 'GET':
        data = select_book(book_id)
        book_name = data.get("name")
        lang_id = data.get("lang_id")
        lang_name = get_info_lang(lang_id)
        bc_id = data.get("bc_id")
        book_class = get_info_class(bc_id)
        author_name = select_author(data.get("author_id")).get("author_name")
        book_desc = data.get("desc")
        return jsonify(book_id=book_id, lang_id=lang_id, lang_name=lang_name, book_name=book_name,
                       author_name=author_name,
                       book_class=book_class, book_desc=book_desc)
    elif request.method == 'POST':
        author_id = g.author_id
        data = request.form
        book_name = data.get("name")
        bc_id = data.get("bc_id")
        book_desc = data.get("book_describe")
        # 选择要翻译的语言版本
        new_lang_id = int(data.get("new_lang_id"))
        root_book_id = select_book(book_id)['rootbookid']
        lang_id = int(select_book(book_id).get("lang_id"))
        if new_lang_id == lang_id:
            return jsonify(msg="您选择的翻译语言版本与当前书籍语言版本相同，请重新选择", code=4000)
        else:
            new_book_id = add_book_edition(root_book_id,
                                           booklib(author_id=author_id, name=book_name, lang_id=new_lang_id,
                                                   bc_id=bc_id, desc=book_desc))
            return jsonify(msg="可以开始翻译", new_book_id=new_book_id, code=200)


# 译者翻译界面
@author.route('/translate/<int:book_id>/<int:new_book_id>/<int:c_no>', methods=['GET', 'POST'])
@author_login_required
def translate_book(book_id, new_book_id, c_no):
    # 显示原文
    if request.method == 'GET':
        title = select_bookcontent(book_id, c_no)[0]
        content = select_bookcontent(book_id, c_no)[1]
        return jsonify(content=content, title=title)
    # 提交译文
    elif request.method == 'POST':
        data = request.form
        content_text = data.get("text")
        title = data.get('title')
        if add_content(new_book_id, c_no, title, content_text):
            return jsonify(msg="译文提交成功", code=200)
        else:
            return jsonify(msg="译文提交失败", code=4000)
