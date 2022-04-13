from telethon import events
from time import sleep
from selenium import webdriver
import asyncio
from os import remove

@events.register(events.NewMessage(outgoing=True, pattern=r'\.wps'))
async def runwps(event):
    await event.edit("Processing...")
    webpage = event.message.raw_text.split()
    messagelocation = event.to_id
    screenshotfilename = "screenshotbyridogram.png"
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = "/app/.apt/usr/bin/google-chrome"
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        await event.edit("Starting Google Chrome...")
        driver = webdriver.Chrome(executable_path="/app/.chromedriver/bin/chromedriver", chrome_options=chrome_options)
        sleep(2)
        driver.get(f"{webpage[1]}")
        await event.edit("Calculating Web Page Dimensions...")
        height = driver.execute_script(
            "return Math.max(document.body.scrollHeight, document.body.offsetHeight, "
            "document.documentElement.clientHeight, document.documentElement.scrollHeight, "
            "document.documentElement.offsetHeight);")
        width = driver.execute_script(
            "return Math.max(document.body.scrollWidth, document.body.offsetWidth, "
            "document.documentElement.clientWidth, document.documentElement.scrollWidth, "
            "document.documentElement.offsetWidth);")
        driver.set_window_size(width + 125, height + 125)
        sleep(2)
        waitforcalculating = height / 1000
        await event.edit("Taking Screenshot...")
        await asyncio.sleep(int(waitforcalculating))
        driver.save_screenshot(screenshotfilename)
        await event.edit("Stoppping Google Chrome...")
        driver.close()
        await event.delete()
        await event.client.send_file(messagelocation, screenshotfilename)
        remove(screenshotfilename)
    except:
        pass
