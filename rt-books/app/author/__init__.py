from flask import Blueprint

# 创建蓝图对象
author = Blueprint("author", __name__)  # 作者蓝图对象

from . import api
