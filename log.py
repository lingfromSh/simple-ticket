"""
python3 logging 日志模块
doc: https://docs.python.org/3/library/logging.html
"""

import logging

"""
lineno 行数
levelno 提示等级
asctime 时间
name logger名字
message 消息
"""
logger = logging.getLogger("ticket")

file_handler = logging.FileHandler(filename="log.log",
                                   encoding="utf-8")

formatter = logging.Formatter(
    fmt="%(lineno)d %(levelno)s %(asctime)s %(name)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S %a"
)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
