"""
Python3
仅用于学习,请不要用作其他商业用途.
"""
import subprocess
from log import logger
from sites import *

try:
    """Fire是一个方便搭建命令行的第三方包"""
    from fire import Fire
except ImportError:
    logger.info("缺少Click, 安装中")
    subprocess.run("pip3 install Fire")


class CLI:
    """脚手架"""

    @classmethod
    def register(cls, count=1, quiet=False, multiprocesses=1, interval=30, use_proxy=False):
        """
        注册帐号
        :@param quiet: 静默注册
        :@param multiprocesses: 多线程数， 1=单线程
        :@param interval: 每轮注册间隔 (s/秒)
        :@param use_proxy: 是否使用proxy
        """
        pass

    @classmethod
    def login(cls, count=1, quiet=False, multiprocesses=1, interval=30, use_proxy=False):
        """
        登录帐号
        :@param quiet: 静默登录
        :@param multiprocesses: 多线程数， 1=单线程
        :@param interval: 每轮注册间隔 (s/秒)
        :@param use_proxy: 是否使用proxy
        """
        pass

    @classmethod
    def vote(cls, count=1, quiet=False, multiprocesses=1, interval=30, use_proxy=False):
        """
        登录帐号
        :@param quiet: 静默登录
        :@param multiprocesses: 多线程数， 1=单线程
        :@param interval: 每轮注册间隔 (s/秒)
        :@param use_proxy: 是否使用proxy
        """
        pass
    
    @classmethod
    def browser(cls, count=1, quiet=False, multiprocesses=1, interval=30, use_proxy=False):
        """
        模仿人工浏览网站
        科学爬虫，实现双赢
        """
        pass

Fire(CLI)