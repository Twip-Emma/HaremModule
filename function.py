'''
Author: your name
Date: 2021-07-17 09:57:53
LastEditTime: 2021-07-24 11:24:24
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \027MyWife\function.py
'''
from pack import *


class Function:
    # 获取老婆功能组
    def func_get_new_wife(self,user_id,user_name):
        a = UserInfo(user_id,user_name)
        a.show_wifes()
        flag = a.get_new_wife_check()
        if flag == "WifeNumError":
            return "你的老婆数量达到上限，无法获取"
        elif flag == "UserSbgDoNotEnought":
            return "你的渣男值过高，无法获取"
        elif flag == "OK":
            return "你成功获取到了老婆"

    # 和老婆互动功能组
    def func_change_mood(self,wife_id,user_id):
        a = UserInfo(user_id)
        mood = random.randint(1,100)
        if mood <10:
            a.wife_mood_change(wife_id)
        pass
