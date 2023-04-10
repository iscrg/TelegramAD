from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import os, sys
import csv
import time

#Trying connect to Telegram.
try:
    api_id = 11111111
    api_hash = '***'
    phone = '****'
    client = TelegramClient(phone, api_id, api_hash)
    client.connect()
except KeyError:
    print('[!] Login error! Please check account.')
 
#Setting parameters.
os.system('clear')
chats = []
last_date = None
chunk_size = 200
groups=[]

#Read chats.
result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)

#Write chats to chat list.
for chat in chats:
    try:
        if chat.megagroup== True:
            groups.append(chat)
    except:
        continue
 
#Select chat.
print('[+] Choose a group to scrape members :')
i=0
for g in groups:
    print(f'[{str(i)}] - {g.title}')
    i+=1
 
print('')
g_index = input('[+] Enter a Number : ')
target_group=groups[int(g_index)]
 
#Getting members.
print('[+] Fetching Members...')
time.sleep(1)
all_participants = []
all_participants = client.get_participants(target_group)
 
#Write members to scv file.
print('[+] Saving In file...')
time.sleep(1)
with open("members.csv","w",encoding='UTF-8') as f:
    writer = csv.writer(f,delimiter=",",lineterminator="\n")
    writer.writerow(['username','user id', 'access hash','name','group', 'group id'])
    for user in all_participants:
        if user.username:
            username= user.username
        else:
            username= ""
        if user.first_name:
            first_name= user.first_name
        else:
            first_name= ""
        if user.last_name:
            last_name= user.last_name
        else:
            last_name= ""
        name= (first_name + ' ' + last_name).strip()
        writer.writerow([username,user.id,user.access_hash,name,target_group.title, target_group.id])      
print('[+] Members scraped successfully.')
