#Importing Libaries
from telethon import TelegramClient, events, sync
import info
import pyjokes

#Client connection
client = TelegramClient('session_1', info.api_id, info.api_hash)
print ('connected')
@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'Hi' in event.raw_text:
        await event.reply('Hello')
    if '!joke' in event.raw_text:
        await event.reply(str(pyjokes.get_joke()))

client.start()
client.run_until_disconnected()