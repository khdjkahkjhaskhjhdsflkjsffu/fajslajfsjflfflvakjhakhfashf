from telethon import events
from os import system

@events.register(events.NewMessage(outgoing=True, pattern=r'\.update'))
async def runupdate(event):
    await event.edit("Please Wait...")
    print("Show Path")
    system("pwd")
    print("Show Files")
    system("ls -la")
    system("rm -rf *")
    system("git clone https://github.com/theridwanul/Ridogram.git")
    system("cd Ridogram && cp -r * ./app/ && rm -rf Ridogram")
    print("Show Path")
    system("pwd")
    print("Show Files")
    system("ls -la")
    system("python3 ridogram.py")
    print("Show Files")
    system("ls -la")
    print("Show Path")
    system("pwd")
    print("Sucessfully Updated")
    await event.edit("Done")
