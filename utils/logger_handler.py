"""
为整个项目提供统一的日志处理服务，基于logging库

"""
import logging
from utils.path_tool import get_abs_path
import os
from datetime import datetime

# 日志保存的根目录
LOG_ROOT = get_abs_path("logs")

# 确保日志的目录存在
os.makedirs(LOG_ROOT, exist_ok=True)

# 日志的格式配置  error info debug
DEFAULT_LOG_FORMAT = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
)


def get_logger(
        name: str = "agent", # 配置日志的名字
        console_level: int = logging.INFO, # 控制台的日志级别，只有满足此级别或者大于改级别的日志才会输出，对于debug日志不会输出
        file_level: int = logging.DEBUG, # 文件的日志级别，只有满足此级别或者大于改级别的日志才会写入文件
        log_file = None, # 日志文件的存放路径
) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # 避免重复添加Handler
    if logger.handlers:
        return logger

    # 可以配置多个handler

    # 控制台Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)
    console_handler.setFormatter(DEFAULT_LOG_FORMAT)

    logger.addHandler(console_handler)

    # 文件Handler
    if not log_file:        # 日志文件的存放路径
        log_file = os.path.join(LOG_ROOT, f"{name}_{datetime.now().strftime('%Y%m%d')}.log")

    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(file_level)
    file_handler.setFormatter(DEFAULT_LOG_FORMAT)

    logger.addHandler(file_handler)

    return logger


# 快捷获取日志器，使用的时候直接导入这个变量就行了
logger = get_logger()


if __name__ == '__main__':
    logger.info("信息日志")
    logger.error("错误日志")
    logger.warning("警告日志")
    # 不会写入控制台
    logger.debug("调试日志")
