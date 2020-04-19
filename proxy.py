import requests
from log import logger

__all__ = ["XiaoXiangProxyClientFactory", "YuanRenYunProxyClientFactory"]


class ProxyClient:
    API_HOST = ""

    def get_proxy(self, count=1):
        """失败返回-1 成功返回代理ip数据"""
        raise NotImplementedError


class XiaoXiangProxyClient(ProxyClient):
    API_HOST = "https://api.xiaoxiangdaili.com/"
    API_GET_PROXY = "ip/get/"

    def __init__(self, appkey=None, appsecret=None):
        self.appkey = appkey
        self.appsecret = appsecret

    def get_proxy(self, count):
        params = {
            'appKey': self.appkey,
            'appSecret': self.appsecret,
            'wt': 'json',
            'method': 'http',
            'cnt': count
        }
        try:
            resp = requests.get(self.API_HOST + self.API_GET_PROXY,
                                params=params)
            if resp.status_code == 200 and resp.json().get("code") == 200:
                logger.info("Get a new proxy ip")
                return resp.json()
        except requests.exceptions.RequestException:
            logger.info("HTTP Request failed.")
            return -1


class YuanRenYunProxyClient(ProxyClient):
    API_HOST = "http://tunnel-api.apeyun.com/"
    API_GET_PROXY = "q"

    def __init__(self, appkey=None, appsecret=None):
        self.appkey = appkey
        self.appsecret = appsecret

    def set_appkey(self, appkey=None):
        self.appkey = appkey

    def set_appsecret(self, appsecret=None):
        self.appsecret = appsecret

    def get_proxy(self, count):
        params = {
            "id": self.appkey,
            "secret": self.appsecret,
            "limit": count,
            "format": "json",
            "auth_mode": "auto"
        }
        try:
            response = requests.get(
                url=self.API_HOST + self.API_GET_PROXY,
                params=params,
            )
            if response.status_code == 200 and response.json().get("code") == 200:
                logger.info("Get a new proxy ip")
                return response.json()
        except requests.exceptions.RequestException:
            logger.info("HTTP Request failed.")
            return -1


class ProxyClientFactory:
    """代理客户端工厂类"""

    @staticmethod
    def create(appkey, appsecret):
        raise NotImplementedError


class XiaoXiangProxyClientFactory(ProxyClientFactory):
    """小象代理客户端工厂类"""

    @staticmethod
    def create(appkey, appsecret):
        return XiaoXiangProxyClient()


class YuanRenYunProxyClientFactory(ProxyClientFactory):
    """猿人云代理客户端工厂类"""

    @staticmethod
    def create(appkey, appsecret):
        return YuanRenYunProxyClient()

