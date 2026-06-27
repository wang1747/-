# 直接操作数据库的脚本：建表并插入一条测试数据
import sqlite3

conn=sqlite3.connect('study.db')
cursor=conn.cursor()

cursor.execute('''
create table if not exists study_logs(
        id integer primary key autoincrement,
        data text,
        subject text,
        hours real,
        notes text
    )
''')

cursor.execute(
        "insert into study_logs(data, subject, hours, notes) values(?,?,?,?)",
        ("2026-6-26","sql",2.5,"学习SQL基础语法")
)

conn.commit()
conn.close()
