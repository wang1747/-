# 数据库操作模块（原 2.py，因 Python 不允许数字开头的模块名而改名）
#负责数据库操作
import sqlite3

db_name='study_logs.db'

def init_db():
        conn=sqlite3.connect(db_name)
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
        conn.commit()
        conn.close()


def add_logs(date,subject,hours,notes):
        conn=sqlite3.connect(db_name)
        cursor=conn.cursor()
        cursor.execute("insert into study_logs(data, subject, hours, notes) values(?,?,?,?)",
                       (date, subject, hours, notes))
        conn.commit()
        conn.close()


def get_logs():
        conn=sqlite3.connect(db_name)
        cursor=conn.cursor()
        cursor.execute("select * from study_logs")
        logs=cursor.fetchall()
        conn.close()
        return logs

# 模块自测：直接运行本文件时初始化并插入一条测试数据
if __name__=='__main__':
        init_db()
        add_logs("2026-6-26","sql",2,"学习SQL基础语法")
        print(get_logs())


def get_logs_by_subject(subject):
        conn=sqlite3.connect(db_name)
        cursor=conn.cursor()
        cursor.execute("select * from study_logs where subject=?", (subject,))
        logs=cursor.fetchall()
        conn.close()
        return logs



def get_total_hours():
        conn=sqlite3.connect(db_name)
        cursor=conn.cursor()
        cursor.execute("select sum(hours) from study_logs")
        logs=cursor.fetchall()
        conn.close()
        return logs


def get_weekly_hours():
        conn=sqlite3.connect(db_name)
        cursor=conn.cursor()
        cursor.execute("select sum(hours) from study_logs where data >= date('now', '-7 days')")
        logs=cursor.fetchall()
        conn.close()
        return logs




