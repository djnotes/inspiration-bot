import time
import math

from pyrogram import Client, filters



from apscheduler.schedulers.asyncio import AsyncIOScheduler

import random

app = Client("session/bot")

subscriber_id = ''
subscriber_telegram_id = ''



start_time = time.time()

def randomInspiration():
    phrases = [
        "Wake up and work",
        "Every second matters",
        "Today, you will go one step closer to your goal",
        "Wake up! Today is an important day",
        "Every big goal starts with a dream. Move toward your dream!",

    ]
    return phrases[random.randint(0, phrases.__len__() - 1)]

async def job():
    global subscriber_telegram_id
    global subscriber_id
    if(app.is_initialized):
        lifetime = math.ceil(time.time() - start_time)
        if lifetime <= 3600:
            message = f"My age: {math.floor(lifetime)} seconds"
        elif  3600 <= lifetime and lifetime <= 86400:
            message = f"My age: {math.floor(lifetime / 3600)} hours"
        else:
            message = f"My age: {math.floor(lifetime / 86400)} days"
        await app.send_message(subscriber_id, randomInspiration() +  f"\n{message}")
        peer = subscriber_telegram_id if subscriber_telegram_id else subscriber_id
        await app.send_message('djnotes', f'Inspiration sent to {peer}')
        #TODO: Save message and sending time in database
        # await app.send_message(id, f"My age: {time.time() - start_time} seconds")


scheduler = AsyncIOScheduler()
scheduler.add_job(job, "interval", seconds = 3)


@app.on_message(filters.private)
async def handle(client, message):
    global scheduler
    global subscriber_id
    global subscriber_telegram_id
    if(message.text == '/start'):
        subscriber_id = message.from_user.id
        scheduler.start()
        await client.send_message('djnotes', f'Inspiration sent to {subscriber_id}')
        #TODO: Get user's Telegram ID and save it in receiver_telegram_id
        #TODO: Save the user in database
        

    elif(message.text == '/stop'):
        scheduler.stop()

app.run()


