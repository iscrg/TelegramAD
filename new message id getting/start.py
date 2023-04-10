from telethon.sync import TelegramClient, events
import telebot

#Connect to Telegram account.
api_id = 16300155 
api_hash = '351d4dcd207b3ba204a58638cc2f1406'
phone_number = '79952720752'
client = TelegramClient(phone_number, api_id, api_hash)
client.connect()

#Search new message and print it's ID.
@client.on(events.NewMessage(1861197001))
async def handler(event):
    message_id = 'ID: ' + str(event.id)
    print(message_id)
    await client.send_message('79639471107', message_id)
client.run_until_disconnected()