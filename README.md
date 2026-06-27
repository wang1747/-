# 学习记录管理系统

一个基于 Python 和 SQLite 的命令行学习记录管理工具，用于记录和统计每日学习时间。

## 文件结构

| 文件 | 说明 |
|------|------|
| `main.py` | 主程序入口，提供交互式菜单界面 |
| `database.py` | 数据库操作模块，封装建表、增删改查等函数 |
| `schemas.py` | Pydantic 数据模型 |
| `requirements.txt` | 项目依赖 |

## 运行方式

```bash
# 启动菜单程序
python main.py

# 单独测试数据库模块
python database.py
```

## 功能

1. 添加学习记录（日期、科目、小时数、备注）
2. 查看所有记录
3. 按科目筛选记录
4. 查看总学习时间
5. 查看本周学习时间

还没有实现输入相同数据提醒的功能，可能会有大量重复数据

## API 模式

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
