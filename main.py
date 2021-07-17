'''
Author: your name
Date: 2021-07-17 10:04:03
LastEditTime: 2021-07-17 10:14:27
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \027MyWife\main.py
'''
from nonebot import (CommandSession, MessageSegment, NoticeSession,NLPSession,
                     RequestSession, get_bot, on_command, on_notice,on_natural_language,
                     on_request)
from nonebot.permission import *
# from bot_config import GROUP_USE


@on_command('harem_info', aliases=('后宫情况','后宫信息'),only_to_me=False)
async def _(session: CommandSession):
    session.finish()


@on_command('harem_info', aliases=('前往储秀阁','储秀阁'),only_to_me=False)
async def _(session: CommandSession):
    session.finish()


# 自然语言处理
@on_natural_language(only_to_me=True)
async def _(session: NLPSession):
    pass

