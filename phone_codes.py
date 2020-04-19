"""
接收手机验证码类
"""


class PhoneCodeClient:
    # 接码平台的api根地址
    API_HOST = None
    # ...其他子api地址
    _instance = None

    def __new__(cls, *args, **kwargs):
        """应该一个平台api只能有一个client对接"""
        if not getattr(cls, "_instance"):
            parent = super()
            cls._instance = parent.__new__(*args, **kwargs)
        return cls._instance

    def get_mobile(self, count=1, **kwargs):
        """
        获得接验证码的手机号
        """
        raise NotImplementedError

    def release(self, mobile=None):
        """
        释放一个指定的手机号
        """
        raise NotImplementedError

    def release_all(self):
        """
        释放所有手机号
        """
        raise NotImplementedError

    def add_to_blacklist(self, mobile):
        """
        拉黑一个手机号
        """
        raise NotImplementedError
