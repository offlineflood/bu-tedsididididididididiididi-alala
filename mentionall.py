import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from asyncio import sleep
from Config import Config

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN
bot_username = Config.BOT_USERNAME
support = Config.SUPPORT_CHAT
owner = Config.OWNER_USERNAME
bot_name = Config.BOT_NAME


SUDO_USERS = Config.SUDO_USERS

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

anlik_calisan = []

tekli_calisan = []

@client.on(events.NewMessage(pattern="^salam$"))
async def start(event):
  await event.reply("**🤖Salam Mən [Usta Taggger Bot](http://t.me/ustataggerbot)-u.**\n**Qurupunuz'daki  bütün üzvləri tağ etmək səlahiyyətinə sahibəm.\n\n🤖Əmrlər üçün /help yazıb məndən kömək ala bilərsiniz.**",
              



print(">> Bot işləyir narahat olmayın. @ThrHassan Məlumat almaq üçün <<")
client.run_until_disconnected()
