from telethon import events, Button, custom
import re, os
from MashaRoBot.events import register
from MashaRoBot import telethn as tbot
from MashaRoBot import telethn as tgbot
PHOTO = "https://telegra.ph/file/1827ec3f0fd066a7c2874.jpg"
@register(pattern=("/alive"))
async def awake(event):
  WOLFX = event.sender.first_name
  WOLFX = "**đş đ đđŚ, đđ¨đĽđđ âď¸** \n\n"
  WOLFX += "**đş đđ¨đĽđđ đđŹ đđđŤđđđđ­đĽđ˛ đđ¨đ°đĽđ˘đ§đ **\n\n"
  WOLFX += "**đş đđ¨đĽđđ : 2.0 đđđđđđ**\n\n"
  WOLFX += "**đş đđ˛ đđ°đ§đđŤ :** [Há´á´á´á´Ę 888+](https://t.me/HMF_OWNER_1)\n\n"
  WOLFX += "**đş đđđĽđđ­đĄđ¨đ§ đđđŤđŹđ˘đ¨đ§ : 1.23.0**\n\n"
  BUTTON = [[Button.url("đđđđđđđđĄď¸", "https://t.me/wolfxbotz"), Button.url("đđđđđđđ¨âđť", "https://t.me/joinchat/r9qx47U5xEZjY2E1")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=WOLFX,  buttons=BUTTON)
