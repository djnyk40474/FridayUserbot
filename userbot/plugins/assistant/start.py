#    Copyright (C) Midhun KM 2020
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
# 
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from telethon import events, custom, Button
from telethon.tl.types import (
    Channel,
    Chat,
    User
)

import emoji
import asyncio
from googletrans import Translator
import re
import io
from math import ceil
from userbot.plugins import inlinestats
from telethon import custom, events, Button
from userbot import CMD_LIST
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd
from telethon.utils import get_display_name
from userbot.utils import admin_cmd, sudo_cmd
from userbot.uniborgConfig import Config
from telethon import events
from datetime import datetime
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd
import time
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from userbot import Lastupdate, bot
from userbot.plugins.sql_helper.botusers_sql import add_me_in_db, his_userid
from userbot.plugins.sql_helper.idadder_sql import add_usersid_in_db, get_all_users

@tgbot.on(events.NewMessage(pattern="^/start"))
async def start(event):
    starkbot = await tgbot.get_me()
    bot_id = starkbot.first_name
    vent = event.chat_id
    starttext = (f"Hello, I am {bot_id} , An Powerfull Assistant Bot to Serve My [Master](tg://user?id={bot.uid}) \nAll Messages That you Send here is forwarded to my master \nPlease Be Polite To My Master Else You Know !")
    if event.from_id == bot.uid:
        await tgbot.send_message(
           vent,
           message=f"Hi Master, It's Me {bot_id}, Your Assistant ! \nWhat You Wanna Do today ?",
           buttons = [
           [custom.Button.inline("Show Users 🔥", data="users")],
           [custom.Button.inline("Commands For Assistant", data="gibcmd")],
           [Button.url("Join Channel 📃", "t.me/Fridayot")]
            ]
           )
    else:
        await tgbot.send_message(
           event.chat_id,
           message=starttext,
           link_preview=False,
           buttons = [
           [custom.Button.inline("Deploy your Friday 🇮🇳", data="deploy")],
           [Button.url("Help Me ❓", "t.me/Fridayot")]
       ]
      )


# Data's

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"deploy")))
async def help(event):
        await event.delete()
        if event.query.user_id is not bot.uid:
            await tgbot.send_message(
                event.chat_id,
                message="You Can Deploy Friday In Heroku By Following Steps Bellow, You Can See Some Quick Guides On Support Channel Or On Your Own Assistant Bot. \nThank You For Contacting Me.",
                buttons = [
                [Button.url("Deploy Tutorial 📺", "https://youtu.be/xfHcm_e92eQ")],
                [Button.url("Need Help ❓", "t.me/FridaySupportOfficial")]
                 ]
                )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"users")))
async def users(event):
         if event.from_id == bot.uid:
             await event.delete()
             total_users = get_all_users()
             users_list = "List Of Total Users In Bot. \n\n"
             for starked in total_users:
                 users_list += ("==> {} \n").format(int(starked.chat_id))
             with io.BytesIO(str.encode(users_list)) as tedt_file:
                 tedt_file.name = "userlist.txt"
                 await tgbot.send_file(
                     event.chat_id,
                     tedt_file,
                     force_document=True,
                     allow_cache=False
                     )
         else:
            pass
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"gibcmd")))
async def users(event):
         await event.delete()
         grabon = "Hello Here Are Some Commands \n➤ /start - Check if I am Alive \n➤ /ping - Pong! \n➤ /tr <lang-code> \n➤ /broadcast - Sends Message To all Users In Bot \n➤ /id - Shows ID of User And Media. \n➤ /addnote - Add Note \n➤ /notes - Shows Notes \n➤ /rmnote - Remove Note "
         await tgbot.send_message(
             event.chat_id,
             grabon
         )
             

# Bot Permit.
@tgbot.on(events.NewMessage(func=lambda e: e.is_private))
async def all_messages_catcher(event):
    if event.raw_text.startswith("/"):
        pass
    elif event.from_id == bot.uid:
        pass
    else:
        sender = await event.get_sender()
        chat_id = event.chat_id
        sed = await event.forward_to(bot.uid)

# Add User To Database ,Later For Broadcast Purpose
# (C) @SpecHide
        add_me_in_db(
            sed.id,
            event.from_id,
            event.id
        )

        add_usersid_in_db(
            event.from_id
        )



# Test 
@tgbot.on(events.NewMessage(func=lambda e: e.is_private))
async def sed(event):
    if event.raw_text.startswith("/"):
        pass
    elif event.from_id == bot.uid:
        msg = await event.get_reply_message()
        real_nigga = msg.id
        msg_s = event.raw_text
        user_id, reply_message_id = his_userid(
        msg.id
        )
        await tgbot.send_message(
        user_id,
        msg_s
        )
    else:
        pass

# broadcast
@tgbot.on(events.NewMessage(pattern="^/broadcast ?(.*)", func=lambda e: e.is_private and e.sender_id == bot.uid))
async def sedlyfsir(event):
    msgtobroadcast = event.pattern_match.group(1)
    userstobc = get_all_users()
    error_count = 0
    sent_count = 0
    for starkcast in userstobc:
        try:
            sent_count += 1
            await tgbot.send_message(int(starkcast.chat_id), msgtobroadcast)
            await asyncio.sleep(0.2)
        except Exception as e:
            try:
                 logger.info(f"Error : {error_count}\nError : {e} \nUsers : {chat_id}"
                 )
            except:
                 pass
    await tgbot.send_message(
        event.chat_id,
        f"Broadcast Done in {sent_count} Group/Users and I got {error_count} Error and Total Number Was {len(userstobc)}"
        )
