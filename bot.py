from telethon import TelegramClient,sync,events
from time import sleep
import requests
from senhas import api_hash,api_id

session = 'Repassar Mensagem'

def main():
    print('Monitoramento iniciado...')
    client = TelegramClient(session,api_id,api_hash)
    @client.on(events.NewMessage(chats = [1001914167270]))
    async def send_message(event):
        if event.media:
            await client.send_file(1002031291944,file = event.media,caption=event.raw_text.replace('https://reurl.cc/K3pApM','http://bit.ly/VipSlotsPagante'))
        else:  
            await client.send_message (1002031291944,event.raw_text.replace('https://reurl.cc/K3pApM','http://bit.ly/VipSlotsPagante'))
    client.start()
    client.run_until_disconnected()

main()



