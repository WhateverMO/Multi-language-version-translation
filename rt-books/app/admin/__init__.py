from flask import Blueprint

# 创建蓝图对象
admin = Blueprint("admin", __name__)  # 管理员蓝图对象

from . import api