import functools
from flask import session, jsonify, g, make_response
from datetime import timedelta
from flask import current_app, request


# 用户验证登录状态的“装饰器”
def user_login_required(view_func):
    @functools.wraps(view_func)
    def wrapper(*args, **kwargs):
        # 判断用户登陆状态
        user_id = session.get("user_id")
        # 如果用户是登陆的，则执行该视图函数
        if user_id is not None:
            # 将user_id保存到g对象中，在视图函数中可以通过g对象获取保存数据
            g.user_id = user_id
            return view_func(*args, **kwargs)
        else:
            # 如果未登录，返回未登录信息
            return jsonify(msg="该用户未登录", code=4000)

    return wrapper


# 作者验证登录状态的“装饰器”
def author_login_required(view_func):
    @functools.wraps(view_func)
    def wrapper(*args, **kwargs):
        # 判断用户登陆状态
        author_id = session.get("author_id")
        # 如果用户是登陆的，则执行该视图函数
        if author_id is not None:
            # 将author_id保存到g对象中，在视图函数中可以通过g对象获取保存数据
            g.author_id = author_id
            return view_func(*args, **kwargs)
        else:
            # 如果未登录，返回未登录信息
            return jsonify(msg="该用户未登录", code=4002)
    return wrapper
