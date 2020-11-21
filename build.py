# -*- coding:utf-8 -*-

"""创建数据库
    Author: github@luochang212
    Date: 2020-11-15
    Usage:
        仅在第一次启动API服务前运行一次
        python build.py
"""

import configparser
import json
import database_handler


def build_bd():
    """创建数据库"""
    config = configparser.ConfigParser()
    config.read('db.conf')
    info = config['DEFAULT']

    dbh = database_handler.DatabaseHandler(db_name=info['db_name'])

    dbh.create_table(
        table_name=info['table_name'],
        columns=json.loads(info['columns']))


if __name__ == '__main__':
    build_bd()
