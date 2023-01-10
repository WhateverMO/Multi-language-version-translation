import random
from flask import request, jsonify, session, g, make_response, render_template, url_for, redirect
from . import user
from ..utils.tool import user_login_required
import os
from datetime import datetime
from werkzeug.utils import secure_filename
from Database import *


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

    user_id = add_user(users(user_name=username, password=password))
    # avatar = url_for('static', filename='img/b2.jpg')  # 这里是默认头像
    # 保存登陆状态到session中
    session["username"] = username
    session["user_id"] = user_id
    # session["user_avatar"] = avatar
    # 返回结果
    return jsonify(msg="注册成功", user_id=user_id, code=200)


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
            return jsonify(msg='账号或密码错误', code=4000)


# 检查登录状态
@user.route('/session', methods=['GET'])
def check_session():
    user_id = session.get("user_id")
    username = session.get("username")
    user_age = session.get("user_age")
    user_gender = session.get("user_gender")
    user_area = session.get("user_area")
    user_describe = session.get("user_describe")
    user_avatar = session.get("user_avatar")
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
    return jsonify(username=username, user_id=user_id, user_age=user_age, user_gender=user_gender,
                   user_area=user_area,
                   user_describe=user_describe, user_phone_number=user_phone_number, user_email=user_email,
                   user_birthday=user_birthday, code=200)


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


# # 用户修改头像  需要有一个单独的提交头像文件的页面
# @user.route('/userinformation/modification/update_avatar', methods=['POST', 'GET'])
# @user_login_required
# def update_user_avatar():
#     if request.method == 'GET':
#         return render_template("checkinformation.html")
#     if request.method == 'POST':
#         user_id = g.user_id
#         # 获取用户上传的头像图片文件
#         image_file = request.files.get("file")
#         # 获取安全的文件名
#         filename = secure_filename(image_file.filename)
#         # 获取上上级路径
#         basedir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
#         # 文件重命名
#         # filename.rsplit('.', 1)[1] 获取文件名的后缀
#         filename = datetime.now().strftime("%Y%m%d%H%M%S") + "_" + str(random.randint(0, 100)) + "." + \
#                    filename.rsplit('.', 1)[1]
#         file_path = basedir + "/app/static/avatar_file/" + filename
#         if image_file is None:
#             return jsonify(msg="未上传图片", code=4000)
#         try:
#             image_file.save(file_path)
#             my_host = "http://127.0.0.1:5000"
#             avatar_url = my_host + "/static/avatar_file/" + filename
#         except Exception as e:
#             print(e)
#             return jsonify(msg="上传图片失败", code=4001)
#         session["picture"] = avatar_url
#         update_user(user_id, {"picture": avatar_url})
#         return jsonify(msg="修改头像成功", user_avatar=avatar_url, code=200)


# 搜索
@user.route('/book/search/<int:book_id>', methods=['GET'])
def book_search(book_id):
    if book_id is None or select_book(book_id) == -1:
        return jsonify(msg='没有找到任何书籍', code=4000)
    else:
        data = select_book(book_id)
        author_name = select_author(data.get('author_id')).get('author_name')
        book_desc = data.get('desc')
        book_name = data.get('name')
        content_list = select_contents_by_a_book(book_id)
        return jsonify(msg='找到书籍', book_name=book_name, author_name=author_name,
                       book_desc=book_desc, content_list=content_list, code=200)


# 书籍简介
@user.route('/read_book/introduce/<string:book_id>', methods=['GET'])
def read_book_index(book_id):
    book_id = int(book_id)
    book_name = select_book(book_id).get("name")
    author_name = select_author(select_book(book_id).get("author_id")).get("author_name")
    cover_path = select_book(book_id).get("cover_path")
    book_describe = select_book(book_id).get("desc")
    # 这里返回所有章节的章节名
    content_list = select_contents_by_a_book(book_id)
    # 例如content_list[0]就对应该书的第一章的章节名
    if content_list == -1:
        return jsonify(msg='该书无章节或该书不存在', code=4000)
    else:
        return jsonify(book_name=book_name, author_name=author_name,
                       book_describe=book_describe, cover_path=cover_path, content_list=content_list, code=200)


# 开始阅读
@user.route('/read_book/start_read/<int:book_id>/<int:c_no>', methods=['POST'])
def start_read(book_id, c_no):
    user_id = request.form.get("user_id")
    time = request.form.get("time")
    title = select_bookcontent(book_id, c_no)[0]
    content_text = select_bookcontent(book_id, c_no)[1]
    if user_id != '0':
        add_user_read_history(user_id, book_id, c_no, time)
        print(get_user_read_history(user_id))
    return jsonify(content_text=content_text, title=title)


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
            book_name = select_book(b_id).get("name")
            author_name = select_author(select_book(b_id).get("author_id")).get("author_name")
            book_desc = select_book(b_id).get("desc")
            book = [book_name, author_name, book_desc, content[index], times[index]]
            books.append(book)
    except Exception as e:
        print(e)
        return jsonify(msg='获取失败，请重试', code=4000)
    if books is None:
        return jsonify(msg='当前无阅读记录', code=200)
    return jsonify(books=books, code=200)


# # 用户创建收藏夹
# @user.route('/create_collection', methods=['POST'])
# @user_login_required
# def create_collection():
#     user_id = g.user_id
#     libname = "默认收藏夹"
#     try:
#         user_create_a_collection_lib(user_id, libname)
#     except Exception as e:
#         print(e)
#         return jsonify(msg='创建失败', code=4000)
#     return jsonify(msg='创建成功', code=200)


# # 用户删除收藏夹
# @user.route('/dele_collection', methods=['POST'])
# @user_login_required
# def dele_collection():
#     user_id = g.user_id
#     libname = request.form.get("libname")
#     try:
#         user_delate_a_collection_lib(user_id, libname)
#     except Exception as e:
#         print(e)
#         return jsonify(msg='删除失败', code=4000)
#     return jsonify(msg='删除成功', code=200)


# 收藏书籍
@user.route('/collect/<int:book_id>', methods=['POST'])
@user_login_required
def collect(book_id):
    user_id = g.user_id
    libname = "默认收藏夹"
    if user_collect_a_book(user_id, libname, book_id):
        return jsonify(msg='收藏成功', code=200)
    else:
        return jsonify(msg='已存在于收藏夹', code=4000)


# 取消收藏
@user.route('/del_collect/<int:book_id>', methods=['POST'])
@user_login_required
def del_collect(book_id):
    user_id = g.user_id
    libname = "默认收藏夹"
    if user_delate_a_collected(user_id, libname, book_id):
        return jsonify(msg='已取消收藏', code=200)
    else:
        return jsonify(msg='已不存在于收藏夹', code=4000)


# 用户收藏界面
@user.route('/get_collection', methods=['GET'])
@user_login_required
def get_collections():
    user_id = g.user_id
    libname = "默认收藏夹"
    try:
        book_ids = get_user_collection(user_id, libname)
        collect_books = []
        for b_id in book_ids:
            book_name = select_book(b_id).get("name")
            author_name = select_author(select_book(b_id).get("author_id")).get("author_name")
            picture = select_book(b_id).get("cover_path")
            book_desc = select_book(b_id).get("desc")
            book = [b_id, book_name, author_name, book_desc, picture]
            collect_books.append(book)
    except Exception as e:
        print(e)
        return jsonify(msg='获取收藏失败，请重试', code=4000)
    return jsonify(collect_books=collect_books, code=200)

# # 用户点开某个收藏夹的界面
# @user.route('/get_collection/<int:libname>', methods=['GET'])
# @user_login_required
# def get_a_collection(libname):
#     user_id = g.user_id
#     try:
#         collection_book_list = get_user_collection(user_id, libname)
#     except Exception as e:
#         print(e)
#         return jsonify(msg='获取失败，请重试', code=4000)
#     return jsonify(collection_book_list=collection_book_list, code=200)

#
#
# # 作者上传书籍封面
# @user.route('/author/add_cover/<int:book_id>/<int:lang_id>', methods=['GET', 'POST'])
# @user_login_required
# def add_cover(book_id, lang_id):
#     if request.method == 'GET':
#         return render_template("")
#     elif request.method == 'POST':
#         author_id = select_author_by_user_id(g.user_id).get('author_id')
#         cover_file = request.files.get("cover_file")
#         filename = secure_filename(cover_file.filename)
#         basedir = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
#         # 获取该lang的英文名
#         for i in select_all_english_lang_id():
#             if i["lang_id"] == lang_id:
#                 book_lang = i["englishlang"]
#         book_dir_name = str(book_id) + '_' + str(author_id)
#         book_lang_dir_name = str(book_lang)
#         # 如果没有原始语言目录就创建
#         if not os.path.exists(basedir + "/app/static/book_file/" + book_lang_dir_name):
#             os.mkdir(basedir + "/app/static/book_file/" + book_lang_dir_name)
#             # 如果没有对应的书籍目录就创建
#         if not os.path.exists(basedir + "/app/static/book_file/" + book_lang_dir_name + '/' + book_dir_name):
#             os.mkdir(basedir + "/app/static/book_file/" + book_lang_dir_name + '/' + book_dir_name)
#         cover_file_path = basedir + "/app/static/book_file/" + book_lang_dir_name + '/' + book_dir_name + "/" + filename
#         cover_file_url = url_for('static',
#                                  filename='book_file/' + book_lang_dir_name + '/' + book_dir_name + '/' + filename)
#         update_book(book_id, author_id, lang_id, {"cover_path": cover_file_url})
#         if cover_file is None:
#             return jsonify(msg="未上传图片", code=4000)
#         try:
#             cover_file.save(cover_file_path)
#             my_host = "http://127.0.0.1:5000"
#             cover_url = my_host + "/app/static/book_file/" + book_lang_dir_name + '/' + book_dir_name + "/" + filename
#         except Exception as e:
#             print(e)
#             return jsonify(msg="上传图片失败", code=4001)
#         return jsonify(msg='上传图片成功', cover_url=cover_file_url, code=200)
