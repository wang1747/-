import sqlite3

db_name='study.db'

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

if __name__=='__main__':
        init_db()
        add_logs("2026-6-26","sql",2,"学习SQL基础语法")
        print(get_logs())