#!/usr/bin/python
# encoding: utf-8
"""
@author: lwqhp
Contact: 
@file: initdata.py
@time:2018/9/9 15:05
"""

from sqlhelper import sqlHelper
from datetime import datetime, timezone

def inster_data(table, datas):
    db = sqlHelper()
    db.clear(table)
    for data in datas:
        db.insert(table, data)
    db.close()

table_poll_question = "polls_question"
datas_poll_question =[ {'id': 1, 'question_text': '你喜欢的游戏是什么?','pub_date':datetime.now()} ]
table_poll_choice = "polls_choice"
datas_poll_choice =[{'id': 1, 'choice_text': '生化危机', 'votes': 0, 'question_id': 1},
                    {'id': 2, 'choice_text': 'GTA5', 'votes': 0, 'question_id': 1},]

def init_data():
    inster_data(table_poll_question, datas_poll_question)

    inster_data(table_poll_choice, datas_poll_choice)

if __name__ == '__main__':
    init_data()