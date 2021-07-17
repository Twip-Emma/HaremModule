from Q7_database import *
from random_config_index import *
import random




# 用户类
class UserInfo:
    # 定义基本属性
    user_id = ""
    user_name = ""
    user_sbg = 0
    user_energy = 0
    user_wife = []

    # 获取这个用户的基本信息
    def __init__(self, user_id, user_name):
        ssql = "select * from user_info where user_id=" + user_id
        sel = sql_dql(ssql)
        if sel == []:
            sql = f"insert into user_info (user_id,user_name,user_sbg,user_energy,wife1_id,wife2_id,wife3_id,wife4_id,wife5_id)"
            sql += f"values('{user_id}','{user_name}',0,100,'0','0','0','0','0')"
            sql_dml(sql)
            sel = sql_dql(ssql)
        print(sel)
        self.user_id = sel[0][0]
        self.user_name = sel[0][1]
        self.user_sbg = sel[0][2]
        self.user_energy = sel[0][3]
        self.user_wife = [sel[0][4], sel[0][5],
                          sel[0][6], sel[0][7], sel[0][8]]

    # 获取新老婆前进行判断
    def get_new_wife_check(self):
        ssql = "select user_sbg from user_info where user_id=" + self.user_id
        sel = sql_dql(ssql)
        sbg = sel[0][0]
        if sbg < 20:
            Wife(self.user_id).get_new_wife()

    # 展示自己的后宫
    def show_wifes(self):
        # ssql = "select user_sbg from user_info where user_id=" + user_id
        msg = ""
        for item in self.user_wife:
            msg += f"{item}\n"
        print(msg)

    # 新用户建立
    def create_new_user(self):
        sql = f"insert into user_info (user_id,user_name,user_sbg,user_energy,wife1_id,wife2_id,wife3_id,wife4_id,wife5_id)"
        sql += f"values('{self.user_id}','{self.user_name}',0,100,'0','0','0','0','0')"
        sql_dml(sql)

    # 销毁实例，释放内存
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, '销毁')


# 老婆类
class Wife:
    # 定义基本属性
    user_id = ""

    def __init__(self, user_id):
        self.user_id = user_id


    def get_new_wife(self):
        if DataBase(self.user_id).get_wife_num() == "wife6_id":
            return False
        wife_height = str(random.randint(145,185))
        wife_name = random.choice(surname) + random.choice(name)
        wife_bud = random.choice(Bud)
        wife_hColor = random.choice(hairColor)
        wife_eyeColor = random.choice(eyeColor)
        wife_hair = random.choice(Hair)
        wife_char = random.choice(Character)
        wife_race = random.choice(race)
        wife_work = random.choice(work)
        wife_oiBai = random.choice(ouBaiSize)
        wife_id = self.user_id + str(random.randint(10000000,99999999))

        # 初始化老婆外观
        wife_appearance = [wife_height,wife_name,wife_bud,wife_hColor,wife_eyeColor,wife_hair,wife_char,wife_race,wife_work,wife_oiBai]
        sql = f"insert into wife_appearance (user_id,wife_id,wife_name,wife_height,wife_bud,wife_hColor,wife_eyeColor,wife_hair,wife_char,wife_race,wife_work,wife_oiBai)"
        sql += f"values('{self.user_id}','{wife_id}','{wife_name}','{wife_height}','{wife_bud}','{wife_hColor}','{wife_eyeColor}','{wife_hair}','{wife_char}','{wife_race}','{wife_work}','{wife_oiBai}')"
        sql_dml(sql)
        msg = "你的新老婆："
        msg += str(wife_appearance)

        # 获取老婆卡槽
        wife_idp = DataBase(self.user_id).get_wife_num() 
        sql = f"update user_info set {wife_idp}='{wife_id}' where user_id={self.user_id}"
        sql_dml(sql)

        # 初始化老婆属性
        sql = f"insert into wife_attribute (user_id,wife_id,wife_life,wife_mood,wife_link,wife_marry,wife_sick)"
        sql += f"values('{self.user_id}','{wife_id}',100,'平静',0,'0','0')"
        sql_dml(sql)

        print(msg)

    # 销毁...
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, '销毁')
        

# 数据库类
class DataBase:
    def __init__(self,user_id) -> None:
        ssql = "select * from user_info where user_id=" + user_id
        sel = sql_dql(ssql)
        self.user_id = sel[0][0]
        self.user_name = sel[0][1]
        self.user_sbg = sel[0][2]
        self.user_energy = sel[0][3]
        self.user_wife = [sel[0][4], sel[0][5],
                          sel[0][6], sel[0][7], sel[0][8]]

    def get_wife_num(self):
        wife_total = 1
        for item in self.user_wife:
            if item != "0":
                wife_total += 1

        wife_id = f"wife{wife_total}_id"
        return wife_id