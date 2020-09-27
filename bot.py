import time
import math


from apscheduler.schedulers.asyncio import AsyncIOScheduler

from pyrogram import Client
import random

app = Client("session/bot")


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
            lifetime = math.ceil(time.time() - start_time)
            if lifetime <= 3600:
                message = f"My age: {math.ceil(lifetime)} seconds"
            elif  3600 <= lifetime and lifetime <= 86400:
                message = f"My age: {math.ceil(lifetime / 3600)} hours"
            else:
                message = f"My age: {math.ceil(lifetime / 86400)} days"
            await app.send_message(id, randomInspiration() +  f"\n{message}")
            # await app.send_message(id, f"My age: {time.time() - start_time} seconds")


scheduler = AsyncIOScheduler()
scheduler.add_job(job, "interval", seconds = 5)
# scheduler.add_job(job, "interval", seconds = 86400)

scheduler.start()

app.run()


