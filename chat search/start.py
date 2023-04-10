from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

#Connect Telegram account.
api_id = 123456789
api_hash = '***'
phone = '79999999999'
client = TelegramClient(phone, api_id, api_hash)

client.connect()

chats = []
last_date = None
chunk_size = 200
groups=[]

#Get dialog list.
result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)
 
for chat in chats:
    try:
        groups.append(chat)
    except:
        continue
 
#Select group and print it's data.
print('[+] Choose a group to scrape members:')
i=0
for g in groups:
    print(f'[{str(i)}] - {g.title}')
    i+=1
 
print('')
grp_index = int(input("[+] Enter a Number : "))
print(f'ID: {str(groups[grp_index].id)}')
print(f'Access_hash: {str(groups[grp_index].access_hash)}')