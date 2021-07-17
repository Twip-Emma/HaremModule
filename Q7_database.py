from os import path
import sqlite3
# from bot_config import ABSOLUTE_PATH

# Q7_database
# KEY_DB_PATH = f"{ABSOLUTE_PATH}\\data\\user_info.db"
KEY_DB_PATH = f"user.db"
# 数据库封装
# 把数据库的操作函数都封装到一个函数里面，避免麻烦


def sql_dql(sql):  # 传入SQL语句并且返回结果
    db = sqlite3.connect(KEY_DB_PATH)  # 链接数据库
    cursor = db.cursor()  # cursor.执行命令
    # try:
    cursor.execute(sql)  # 执行SQL语句
    # fetchall()函数,它的返回值是多个元组,即返回多个行记录,如果没有结果,返回的是()
    result = cursor.fetchall()  # 接收全部的返回结果行
    print(result)
    db.close()  # 关闭数据库
    return result  # 返回结果
    # except:
    #     return {}  # 异常，返回空


def sql_dml(sql):
    db = sqlite3.connect(KEY_DB_PATH)
    cursor = db.cursor()
    # try:
    cursor.execute(sql)  # 执行SQL语句
    res = cursor.fetchone()  # fetchone()函数它的返回值是单个的元组,也就是一行记录,如果没有结果,那就会返回null
    db.commit()  # commit()完成数据库的更新
    db.close()
    # print('1')
    return res
    # except:
    #     db.rollback()  # 回滚
    #     db.close()
    #     return 0