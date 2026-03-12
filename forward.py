from telethon import TelegramClient, events

api_id = 21367965
api_hash = "198b8590c4c2656e8bc4e2b721e71416"

source_group = -1002781143657
target_group = -1003099447280

client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage(chats=source_group))
async def handler(event):
    await client.send_message(target_group, event.message)

client.start()
client.run_until_disconnected()
