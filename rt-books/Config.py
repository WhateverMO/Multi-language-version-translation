import redis


class Config:
    SESSION_TYPE = 'redis'  # 存session进redis
    SESSION_USE_SIGNER = True  # 对cookie中session_id进行隐藏处理 加密混淆
    PERMANENT_SESSION_LIFETIME = 60*60*24*7  # session数据的有效期，单位秒,,, 这里设置的七天有效
    SESSION_REDIS = redis.Redis(host='pukgai.com', port=3306, password="jamkung", db=15)  # 操作的数据库配置
    SECRET_KEY = '12h17fgh726g4d781j9'


# 开发环境
class DevelopmentConfig(Config):
    """开发模式的配置信息"""
    DEBUG = True


# 线上环境
class ProductConfig(Config):
    """生产环境配置信息"""
    pass


config_map = {
    "develop": DevelopmentConfig,
    "product": ProductConfig
}
