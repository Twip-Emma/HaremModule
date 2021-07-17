'''
Author: your name
Date: 2021-07-17 09:57:53
LastEditTime: 2021-07-17 10:02:57
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \027MyWife\__init__.py
'''
from function import *
from pack import *

# user_info 用户表：user_id,user_name,user_sbg,user_energy,wife1_id,wife2_id,wife3_id,wife4_id,wife5_id
# wife_attribute 老婆属性表 user_id,wife_id,wife_life,wife_mood,wife_link,wife_marry,wife_sick
# wife_appearance 老婆外观表 user_id,wife_id,wife_name,wife_bud,wife_hColor,wife_eyeColor,wife_hair,wife_char,wife_race,wife_work,wife_oiBai

user_id = "123456789"
user_name = "张三"
# while True:
    # a = int(input("输入你想运行的功能：\n1.获取老婆\n2.查看后宫\n3.权限更换"))
    # if a==1:
a = UserInfo(user_id,user_name)
a.show_wifes()
a.get_new_wife_check()
# b = UserInfo(user_id,user_name).get_new_wife_check()