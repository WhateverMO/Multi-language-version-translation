from flask import Blueprint

# 创建蓝图对象
user = Blueprint("user", __name__)  # 用户蓝图对象

from . import api
