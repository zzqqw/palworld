from __future__ import annotations

import json
import logging
import os


# 读取环境变量
def osnvironget(env: str) -> str | None:
    val = os.environ.get(env)
    if val is not None:
        if val != "":
            return val
    return None


# 写入文件内容
def writeFile(file: str, contents: str):
    path = os.path.dirname(file)
    if not os.path.exists(path):
        os.makedirs(path)
    with open(file, "w") as f:
        f.write(contents)


# 读取文件内容
def readFile(file: str):
    if not os.path.exists(file):
        logging.error("Unable to find %s file", file)
        raise FileNotFoundError
    with open(file, encoding='utf-8') as f2:
        return f2.read()


def readJSONFile(file: str):
    if not os.path.exists(file):
        logging.error("Unable to find %s file", file)
        raise FileNotFoundError
    with open(file, "r") as f2:
        return json.load(f2)
