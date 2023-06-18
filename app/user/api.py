import pickle
import random
from flask import request, jsonify, session, g, make_response
from . import user
from ..utils.tool import user_login_required
import os
from datetime import datetime
from werkzeug.utils import secure_filename
from Database import *
from app import url_host
from db_struct import *


@user.after_request
def func_res(resp):
    res = make_response(resp)
    res.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    res.headers['Access-Control-Allow-Methods'] = 'GET,POST,DELETE,PUT,OPTIONS'
    res.headers[
        'Access-Control-Allow-Headers'] = 'X-Requested-With, Content-Type, Content-Length, Authorization, Accept, yourHeaderFeild'
    res.headers['Access-Control-Allow-Credentials'] = 'true'
    res.headers['X-Powered-By'] = '3.2.1'
    res.headers['Content-Type'] = 'application/json;charset=utf-8'
    return res


# 用户注册界面
@user.route('/register', methods=['POST'])
def register():
    data = request.form
    username = data.get("username")
    password = data.get("password")
    password2 = data.get("password2")
    # 校验参数
    if not all([username, password, password2]):
        return jsonify(msg="参数不完整", code=4002)

    if password != password2:
        return jsonify(msg="两次密码不一致", code=4001)
    # 这里是默认头像
    my_host = "http://" + url_host
    default_avatar_url = my_host + "/static/avatar_file/b2.jpg"
    user_id = add_user(users(user_name=username, password=password, picture=default_avatar_url))
    # 创建用户的默认收藏夹
    user_create_a_collection_lib(user_id, '默认收藏夹')
    # 保存登陆状态到session中
    session["username"] = username
    session["user_id"] = user_id
    session["picture"] = default_avatar_url
    # 我在这里作了更改，将数据保存为一个对象
    resp = make_response(jsonify(msg="注册成功", user_id=user_id, picture=default_avatar_url, code=200))
    session_bytes = pickle.dumps(session)
    resp.set_cookie('session', session_bytes)
    # 返回结果
    return resp


# 用户登录接口
@user.route('/login', methods=['POST'])
def login():
    data = request.form
    user_id = data.get("user_id")
    password = data.get('password')
    if not all([user_id, password]):
        return jsonify(msg='缺少参数', code=4000)
    else:
        if login_user(user_id, password) == -1:
            return jsonify(msg="账号或密码错误", code=4002)
        elif login_user(user_id, password):
            # 如果验证通过保持登录状态在session中
            session["user_id"] = user_id
            username = select_user(user_id).get("user_name")
            session["username"] = username
            return jsonify(msg="登陆成功", code=200)
        else:
            return jsonify(msg='异常错误', code=4003)


# 检查登录状态
@user.route('/session', methods=['GET'])
def check_session():
    user_id = session.get("user_id")
    username = session.get("username")
    user_age = session.get("user_age")
    user_gender = session.get("user_gender")
    user_area = session.get("user_area")
    user_describe = session.get("user_describe")
    user_avatar = session.get("picture")
    user_phone_number = session.get("user_phone_number")
    user_email = session.get("user_email")
    user_birthday = session.get("user_birthday")

    if user_id is not None:
        return jsonify(user_id=user_id, username=username, user_age=user_age, user_area=user_area,
                       user_gender=user_gender, user_describe=user_describe, user_avatar=user_avatar,
                       user_phone_number=user_phone_number, user_email=user_email, user_birthday=user_birthday,
                       code=200)
    else:
        return jsonify(msg='未登录', code=4000)


# 退出登录
@user.route('/logout', methods=['DELETE'])
@user_login_required  # 验证用户登录的装饰器
def logout():
    if request.method == 'DELETE':
        session.clear()
        return jsonify(msg="成功退出登录", code=200)


# 修改密码
@user.route('/checkpassword', methods=['POST'])
@user_login_required  # 验证用户登录装的饰器
def change_password():
    uid = g.user_id
    data = request.form
    password = data.get("password")
    new_password = data.get("new_password")
    # 校验参数完整
    if not all([new_password, password, uid]):
        return jsonify(msg="参数不完整", code=4000)
    if select_user(uid) == -1:
        return jsonify(msg="获取用户信息失败", code=4000)
    # 用数据库里的密码与用户输入的密码进行对比验证
    if not login_user(uid, password):
        return jsonify(msg='原始密码错误', code=4000)
    # 修改密码
    update_user(uid, {"password": new_password})
    return jsonify(msg='修改成功', code=200)


# 用户查看基本信息
@user.route('/information', methods=['GET'])
@user_login_required  # 验证用户登录的装饰器
def get_user_information():
    # 从管道获取user的id
    user_id = g.user_id
    data = select_user(user_id)
    username = data.get("user_name")
    user_age = data.get("age")
    user_gender = data.get("gender")
    user_area = data.get("area")
    user_describe = data.get("user_describe")
    user_phone_number = data.get("phone_number")
    user_email = data.get("email")
    user_birthday = data.get("birthday")
    user_avatar = data.get("picture")
    following_count = data.get('following_count')
    libs = user_get_all_collection_lib(user_id)
    collect_count = 0
    for lib in libs:
        collect_count += len(get_user_collection(user_id, lib))
    return jsonify(username=username, user_id=user_id, user_age=user_age, user_gender=user_gender,
                   user_area=user_area,
                   user_describe=user_describe, user_phone_number=user_phone_number, user_email=user_email,
                   user_birthday=user_birthday, user_avatar=user_avatar, following_count=following_count,
                   collect_count=collect_count, code=200)


# 用户修改基本信息
@user.route('/information/modification', methods=['POST'])
@user_login_required  # 验证用户登录的装饰器
def update_user_information():
    # 从管道获取user的id
    user_id = g.user_id
    # 获取用户修改的信息
    data = request.form
    username = data.get("username")
    user_age = data.get("user_age")
    user_gender = data.get("gender")
    user_area = data.get("area")
    user_describe = data.get("user_describe")
    user_phone_number = data.get("user_phone_number")
    user_email = data.get("user_email")
    user_birthday = data.get("user_birthday")
    update_user(user_id,
                {"user_name": username, "age": user_age, "gender": user_gender, "area": user_area,
                 "user_describe": user_describe,
                 "phone_number": user_phone_number, "email": user_email, "birthday": user_birthday})
    # 保存成功并返回
    session["username"] = username
    session["user_age"] = user_age
    session["user_gender"] = user_gender
    session["user_area"] = user_area
    session["user_describe"] = user_describe
    session["user_phone_number"] = user_phone_number
    session["user_email"] = user_email
    session["user_birthday"] = user_birthday
    return jsonify(msg="保存成功", username=username, user_id=user_id, user_age=user_age, user_gender=user_gender,
                   user_area=user_area,
                   user_describe=user_describe, user_phone_number=user_phone_number, user_email=user_email,
                   user_birthday=user_birthday, code=200)


# 用户修改头像
@user.route('/information/modification/update_avatar', methods=['POST'])
@user_login_required
def update_user_avatar():
    if request.method == 'POST':
        user_id = g.user_id
        # 获取用户上传的头像图片文件
        image_file = request.files.get("file")
        # 获取安全的文件名
        filename = secure_filename(image_file.filename)
        # 获取上上级路径
        basedir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
        # 文件重命名
        filename = "user_" + str(user_id) + "." + filename.rsplit('.', 1)[1]
        file_path = basedir + "/app/static/avatar_file/" + filename
        if image_file is None:
            return jsonify(msg="未上传图片", code=4000)
        try:
            image_file.save(file_path)
            my_host = "http://" + url_host
            avatar_url = my_host + "/static/avatar_file/" + filename
        except Exception as e:
            print(e)
            return jsonify(msg="上传图片失败", code=4001)
        session["picture"] = avatar_url
        update_user(user_id, {"picture": avatar_url})
        return jsonify(msg="修改头像成功", user_avatar=avatar_url, code=200)


# 搜索
@user.route('/book/search', methods=['POST'])
def book_search():
    book_name = request.form.get('book_name')
    res = search_book(book_name)
    books = []
    if res:
        for data in res:
            b_id = data.get('b_id')
            lang = get_info_lang(data.get('lang_id'))
            book_class = get_info_class(data.get('bc_id'))
            author_id = data.get("author_id")
            author_name = select_author(author_id).get("author_name")
            desc = data.get('desc')
            cover_path = data.get('cover_path')
            book_name = data.get('name')
            time = data.get('create_time')
            books.append(
                {'book_id': b_id, 'book_class': book_class, 'lang': lang, 'author_id': author_id,
                 'author_name': author_name, 'desc': desc,
                 'cover_path': cover_path, 'book_name': book_name, 'time': time})
        return jsonify(msg='找到有关书籍', books=books, code=200)
    else:
        return jsonify(msg='没有找到任何有关书籍', code=4000)


# 书籍简介页面（含用户评论）
@user.route('/read_book/introduce/<int:book_id>', methods=['GET', 'POST'])
@user_login_required
def read_book_index(book_id):
    if request.method == 'GET':
        data = select_book(book_id)
        book_name = data.get("name")
        author_id = data.get("author_id")
        author_name = select_author(author_id).get("author_name")
        cover_path = data.get("cover_path")
        book_describe = data.get("desc")
        # 书籍评论
        barrage = select_barrage_by_b_id(book_id)
        # 这里返回所有章节的章节名
        content_list = select_contents_by_a_book(book_id)
        # 例如content_list[0]就对应该书的第一章的章节名
        if content_list == -1:
            return jsonify(msg='该书无章节或该书不存在', code=4000)
        else:
            return jsonify(book_name=book_name, author_id=author_id, author_name=author_name,
                           book_describe=book_describe, cover_path=cover_path, content_list=content_list,
                           barrages=barrage, code=200)
    # 用户发送评论
    elif request.method == 'POST':
        user_id = g.user_id
        barrage = request.form.get('barrage')
        add_user_book_barrage(user_books_barrage(user_id=user_id, book_id=book_id, barrage=barrage))
        return jsonify(msg='评论发送成功！', code=200)


# 开始阅读
@user.route('/read_book/start_read/<int:book_id>/<int:c_no>', methods=['POST'])
def start_read(book_id, c_no):
    user_id = request.form.get("user_id")
    time = request.form.get("time")
    data = select_bookcontent(book_id, c_no)
    if data == 0:
        return jsonify(msg='前面没有更多章节了!', code=4000)
    elif data == -2:
        return jsonify(msg='后面没有更多章节了!', code=4001)
    elif data == -1 or data == -3:
        return jsonify(msg='发生错误了!', code=4002)
    else:
        title = data[0]
        content_text = data[1]
        if user_id != '0':
            add_user_read_history(user_id, book_id, c_no, time)
            print(get_user_read_history(user_id))
        return jsonify(content_text=content_text, title=title, code=200)


# 查看阅读记录
@user.route('/read_history', methods=['GET'])
@user_login_required
def read_history():
    user_id = g.user_id
    try:
        book_ids = []
        times = []
        books = []
        content = []
        history_list = get_user_read_history(user_id)
        for list in history_list:
            book_ids.append(list[0])
            content.append(list[1])
            times.append(list[2])
        for index, b_id in enumerate(book_ids):
            data = select_book(b_id)
            book_name = data.get("name")
            author_name = select_author(data.get("author_id")).get("author_name")
            book_desc = data.get("desc")
            book = [book_name, author_name, book_desc, content[index], times[index]]
            books.append(book)
    except Exception as e:
        print(e)
        return jsonify(msg='获取失败，请重试', code=4000)
    if books is None:
        return jsonify(msg='当前无阅读记录', code=200)
    return jsonify(books=books, code=200)


# 用户创建收藏夹
@user.route('/create_collection', methods=['POST'])
@user_login_required
def create_collection():
    user_id = g.user_id
    libname = request.form.get("libname")
    try:
        user_create_a_collection_lib(user_id, libname)
    except Exception as e:
        print(e)
        return jsonify(msg='创建失败', code=4000)
    return jsonify(msg='创建成功', code=200)


# 用户删除收藏夹
@user.route('/dele_collection/<string:libname>', methods=['DELETE'])
@user_login_required
def dele_collection(libname):
    user_id = g.user_id
    try:
        user_delate_a_collection_lib(user_id, libname)
    except Exception as e:
        print(e)
        return jsonify(msg='删除失败', code=4000)
    return jsonify(msg='删除成功', code=200)


# 收藏书籍
@user.route('/collect/<int:book_id>/<string:libname>', methods=['POST'])
@user_login_required
def collect(book_id, libname):
    user_id = g.user_id
    if user_collect_a_book(user_id, libname, book_id):
        return jsonify(msg='收藏成功', code=200)
    else:
        return jsonify(msg='已存在于收藏夹', code=4000)


# 取消收藏
@user.route('/del_collect/<int:book_id>/<string:libname>', methods=['DELETE'])
@user_login_required
def del_collect(book_id, libname):
    user_id = g.user_id
    if user_delate_a_collected(user_id, libname, book_id):
        return jsonify(msg='已取消收藏', code=200)
    else:
        return jsonify(msg='已不存在于收藏夹', code=4000)


# 用户获取所有收藏夹界面
@user.route('/get_collection_lib', methods=['GET'])
@user_login_required
def get_collections():
    user_id = g.user_id
    libs = user_get_all_collection_lib(user_id)
    return jsonify(msg='获取所有收藏夹成功', collections=libs, code=200)


# 用户点开某个收藏夹
@user.route('/get_collection/<string:libname>', methods=['GET'])
@user_login_required
def get_a_collection(libname):
    user_id = g.user_id
    try:
        collection_book_list = get_user_collection(user_id, libname)
        col_books = []
        for id in collection_book_list:
            data = select_book(id)
            picture = data.get('cover_path')
            book_name = data.get('name')
            desc = data.get('desc')
            col_books.append({'book_id': id, 'book_name': book_name, 'picture': picture, 'desc': desc})
    except Exception as e:
        print(e)
        return jsonify(msg='获取失败，请重试', code=4000)
    return jsonify(msg="获取成功", collection_book_list=col_books, code=200)


# 用户在主页发送弹幕
@user.route('/push_barrage', methods=['POST'])
@user_login_required
def push_barrage():
    try:
        user_id = g.user_id
        barrage = request.form.get("barrage")
        add_barrages(user_barrage(user_id=user_id, barrage=barrage))
        return jsonify(msg='发送成功!', code=200)
    except Exception as e:
        print(e)
        return jsonify(msg='发送失败', code=4000)


# 主页获取弹幕
@user.route('/get_barrage', methods=['GET'])
def get_barrage():
    try:
        barrage = select_barrages()
        return jsonify(msg='获取主页弹幕成功!', barrages=barrage, code=200)
    except Exception as e:
        print(e)
        return jsonify(msg='获取弹幕失败！', code=4000)


# 用户关注作者
@user.route('/follow_author/<int:author_id>', methods=['GET'])
@user_login_required
def following_author(author_id):
    user_id = g.user_id
    try:
        add_user_follow_author(fan(user_id=user_id, author_id=author_id))
        return jsonify(msg='关注成功', code=200)
    except Exception as e:
        print(e)
        return jsonify(msg='关注失败', code=4000)


# 用户取消关注
@user.route('/remove_follow_author/<int:author_id>', methods=['GET'])
@user_login_required
def remove_follow_author(author_id):
    user_id = g.user_id
    try:
        remove_user_unfollow_author(user_id, author_id)
        return jsonify(msg='取消成功', code=200)
    except Exception as e:
        print(e)
        return jsonify(msg='取消失败', code=4000)


# 用户查看自己关注的作者
@user.route('/get_followed_author', methods=['GET'])
@user_login_required
def get_followed_author():
    user_id = g.user_id
    try:
        data = get_user_followed_authors(user_id)
        return jsonify(authors=data, code=200)
    except Exception as e:
        print(e)
        return jsonify(msg='出错了,请重试', code=4000)
