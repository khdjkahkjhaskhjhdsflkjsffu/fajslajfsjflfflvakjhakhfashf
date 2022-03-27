from telethon import events
from os import system

@events.register(events.NewMessage(outgoing=True, pattern=r'\.update'))
async def runupdate(event):
    await event.edit("Please Wait...")
    messagelocation = event.to_id
    try:
        system("git clone https://github.com/theridwanul/Ridogram.git")
        system("heroku git:remote -a mrupdatetester")
        system("git push heroku master")
        await event.edit("Update Successfully")
    except:
        pass