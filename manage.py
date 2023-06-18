from app import create_app
from app import myhost
from flask_cors import CORS
from flask_script import Manager  # 管理项目的，额外指定一些命令
from flask_migrate import Migrate, command  # 管理数据库需要的脚本，追踪数据库的变化的脚本
from gevent.pywsgi import WSGIServer
import gevent

app = create_app("develop")

# gevent.monkey.patch_all()


if __name__ == '__main__':
    server = WSGIServer((myhost, 5000), app)
    server.serve_forever()

    # 测试端口
    # app.run(host=myhost, port=5000)
