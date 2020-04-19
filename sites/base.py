"""
定义每个网站类需要的基础方法和属性
"""


class Site:
    HOST = None

    def register(self, proxy=None, **kwargs):
        """具体看具体网站的注册方式"""
        raise NotImplementedError

    def login(self, proxy=None, **kwargs):
        """返回token/session/cookies具体实现看具体网站"""
        raise NotImplementedError

    def vote(self, proxy=None, **kwargs):
        """具体看具体网站的投票方式,并且返回投票结果"""
        raise NotImplementedError

    def browser(self, proxy=None, **kwargs):
        """健康浏览网站"""
        raise NotImplementedError


if __name__ == "__main__":
    client = Site()

    # register
    client.register()

    # login
    token = client.login()

    # vote
    result = client.vote()

    # browser
    client.browser()