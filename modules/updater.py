from telethon import events
from os import system

@events.register(events.NewMessage(outgoing=True, pattern=r'\.update'))
async def runupdate(event):
    await event.edit("Please Wait...")
    system("git clone https://github.com/theridwanul/Ridogram.git")
    system("rm * && cd Ridogram && cp -r * cd .. && python3 ridogram.py")
    print("Sucessfully Updated")
    await event.edit("Done")