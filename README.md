<!--
 * @Author: your name
 * @Date: 2021-07-17 10:20:57
 * @LastEditTime: 2021-07-17 10:37:20
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \027MyWife\README.md
-->
# HaremModule
后宫模块（反正就当玩具玩玩


### 文件结构
>- \__init__.py中提供了测试单元，main.py为大致触发方式
>- pack.py中编写主要方法
>- random_config_index.py为新老婆构建索引
>- keyword中存放词库


### 数据库信息（MySQL）
>- user_info 用户表：user_id,user_name,user_sbg,user_energy,wife1_id,wife2_id,wife3_id,wife4_id,wife5_id
>- wife_attribute 老婆属性表 user_id,wife_id,wife_life,wife_mood,wife_link,wife_marry,wife_sick
>- wife_appearance 老婆外观表 user_id,wife_id,wife_name,wife_bud,wife_hColor,wife_eyeColor,wife_hair,wife_char,wife_race,wife_work,wife_oiBai


### 数据库表
>- CREATE TABLE wife_appearance(user_id varchar(50),wife_id varchar(50),wife_name varchar(50),wife_height varchar(50),wife_bud varchar(50),wife_hColor varchar(50),wife_eyeColor varchar(50),wife_hair varchar(50),wife_char varchar(50),wife_race varchar(50),wife_work varchar(50),wife_oiBai varchar(50))
>- CREATE TABLE wife_attribute(user_id varchar(50),wife_id varchar(50),wife_life int(50),wife_mood varchar(50),wife_link int(50),
wife_marry varchar(50),wife_sick varchar(50))
>- CREATE TABLE user_info(user_id varchar(50),user_name varchar(50),user_sbg int(50),user_energy int(99),wife1_id varchar(50),wife2_id varchar(50),wife3_id varchar(50),wife4_id varchar(50),wife5_id varchar(50))



### 提交贡献
>- 你可以在issues中发一些问答来扩充本仓库的词库
>- 你可以通过PR补全本仓库中未完成的方法
>- 你可以对本仓库现有的方法进行改进
>- 你可以在issues提出扩充内容


### 已实现内容
>- 获得一个新老婆并初始化信息
>- 用户自动创建


### 注意事项
>- 基本上就是整活用的，没太在意细节，大佬勿喷（
>- 欢迎fork本仓库或者提出你的issues
>- 反正闲着也是闲着不如来整活
>- 基本完成后再进行整理
