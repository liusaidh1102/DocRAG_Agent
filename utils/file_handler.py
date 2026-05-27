"""
文件相关的函数工具封装
"""

import os
import hashlib
from utils.logger_handler import logger
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader, TextLoader

'''
根据文件计算文件的32位十六进制的md5值
'''
def get_file_md5_hex(filepath: str):     # 获取文件的md5的十六进制字符串

    if not os.path.exists(filepath):
        logger.error(f"[md5计算]文件{filepath}不存在")
        return

    if not os.path.isfile(filepath):
        logger.error(f"[md5计算]路径{filepath}不是文件")
        return

    md5_obj = hashlib.md5()

    chunk_size = 4096       # 4KB分片，避免文件过大爆内存
    try:
        with open(filepath, "rb") as f:     # 分片的话，必须二进制（rb）读取
            while chunk := f.read(chunk_size):
                md5_obj.update(chunk)

            """
            chunk = f.read(chunk_size)
            while chunk:
                
                md5_obj.update(chunk)
                chunk = f.read(chunk_size)
            """
            md5_hex = md5_obj.hexdigest()
            return md5_hex
    except Exception as e:
        logger.error(f"计算文件{filepath}md5失败，{str(e)}")
        return None

'''
返回文件夹内的文件列表（允许的文件后缀）
比如仅仅返回data文件夹下txt和pdf后缀的文件
'''
def listdir_with_allowed_type(path: str, allowed_types: tuple[str]):
    files = []

    if not os.path.isdir(path):
        logger.error(f"[listdir_with_allowed_type]{path}不是文件夹")
        return allowed_types
    # 列出文件夹内的文件名，判断文件后缀
    for f in os.listdir(path):
        if f.endswith(allowed_types):
            # 传入/data  返回 /data/xxxx.pdf等等
            files.append(os.path.join(path, f))

    return tuple(files)

# 加载 pdf 文件
def pdf_loader(filepath: str, passwd=None) -> list[Document]:
    return PyPDFLoader(filepath, passwd).load()

# 加载 txt 文件
def txt_loader(filepath: str) -> list[Document]:
    return TextLoader(filepath, encoding="utf-8").load()
