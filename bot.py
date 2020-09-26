import time


from apscheduler.schedulers.asyncio import AsyncIOScheduler

from pyrogram import Client
import random

app = Client("bot")


audience_ids = ['djnotes']

start_time = time.time()

def randomInspiration():
    phrases = [
        "Wake up and work",
        "Every second matters",
        "Today, you will go one step closer to your goal",
        "Wake up! Today is an important day"
    ]
    return phrases[random.randint(0, phrases.__len__() - 1)]

async def job():
    if(app.is_initialized):
        for id in audience_ids: 
            await app.send_message(id, randomInspiration())
            await app.send_message(id, f"My age: {time.time() - start_time} seconds")


scheduler = AsyncIOScheduler()
scheduler.add_job(job, "interval", seconds = 86400)

scheduler.start()

app.run()


