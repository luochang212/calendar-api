# -*- coding:utf-8 -*-

"""API 服务
    Author: github@luochang212
    Date: 2020-11-15
    Usage: uvicorn server:app --reload
"""


from fastapi import FastAPI
from pydantic import BaseModel
import configparser
import json

import database_handler
import method


app = FastAPI()


config = configparser.ConfigParser()
config.read('db.conf')
info = config['DEFAULT']

dbh = database_handler.DatabaseHandler(
    db_name=info['db_name'],
    check_same_thread=False)
m = method.Method(conf_file='db.conf')


class Schedule(BaseModel):
    sid: str  # ID
    name: str  # 名称
    content: str  # 内容
    category: str  # 分类
    level: int  # 重要程度, 0: 未定义  1: 低  2: 中  3: 高
    status: float  # 当前进度, 0 <= status <= 1
    creation_time: str  # 创建时间
    start_time: str  # 开始时间
    end_time: str  # 结束时间


@app.get('/')
def index():
    return {'app_name': 'calendar'}


@app.get('/schedules')
def get_schedules():
    return dbh.fetch_all(
        table_name=info['table_name'])


@app.get('/schedules/{schedule_id}')
def get_schedule(schedule_id: str):
    return m.get(dbh, schedule_id)


@app.post('/schedules')
def create_schedule(schedule: Schedule):
    if m.post(dbh, schedule):
        return schedule
    else:
        return {"errno": "1"}


@app.put('/schedules/{schedule_id}')
def update_schedule(schedule_id: str, schedule: Schedule):
    if m.update(dbh, schedule_id, schedule):
        return schedule
    else:
        return {"errno": "2"}


@app.delete('/schedules/{schedule_id}')
def delete_schedule(schedule_id: str):
    if m.delete(dbh, schedule_id):
        return {"msg": "success"}
    else:
        return {"errno": "3"}
