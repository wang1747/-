# 从 database 模块导入所有数据库操作函数
from database import *

def main():
        while True:
                print("\n=== 学习记录管理系统 ===")
                print("1. 添加学习记录")
                print("2. 查看所有记录")
                print("3. 按科目查看")
                print("4. 查看总学习时间")
                print("5. 查看本周学习时间")
                print("6. 退出")

                choice=input("请选择操作：")
                if choice=='1':
                        date=input("请输入日期(格式:YYYY-MM-DD)：")
                        subject=input("请输入科目：")
                        hours=float(input("请输入学习小时数："))
                        notes=input("请输入备注：")
                        add_logs(date,subject,hours,notes)
                elif choice=='2':
                        print(get_logs())
                elif choice=='3':
                        subject=input("请输入科目：")
                        print(get_logs_by_subject(subject))
                elif choice=='4':
                        print(get_total_hours())
                elif choice=='5':
                        print(get_weekly_hours())
                elif choice=='6':
                        break
                else:
                        print("无效选择，请重新输入。")

# 程序入口：先初始化数据库，再启动菜单
if __name__ == '__main__':
    init_db()
    main()