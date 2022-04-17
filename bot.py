import time
import math
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from pyrogram import Client, filters
from pyrogram.types import Message



from apscheduler.schedulers.asyncio import AsyncIOScheduler

import random

from types import Inspiration

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
app = Client("session/bot", api_id = api_id, api_hash=api_hash)

subscriber_id = ''
subscriber_telegram_id = ''



start_time = time.time()

def randomInspiration():
    pass

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
async def handle(client, message: Message):
    global scheduler
    global subscriber_id
    global subscriber_telegram_id
    if(message.text == '/start'):
        subscriber_id = message.from_user.id
        scheduler.start()
        await client.send_message('djnotes', f'Inspiration sent to {subscriber_id}')
        #TODO: Get user's Telegram ID and save it in receiver_telegram_id
        #TODO: Save the user in database
    if (message.text == '/send'):
        # Simple use-case to test functionality by sending a random inspiration to the panel user
        with Session(engine) as session:
          inspirations = session.query(Inspiration).all()
          selected = int (random.random() * len(inspirations))
          message.reply(inspirations[selected].text)
        
          
        

    elif(message.text == '/stop'):
        scheduler.stop()

app.run()




# Load credentials
userEnv = open(os.getenv("MARIADB_USER_FILE")).read()
passwordEnv = open(os.getenv("MARIADB_PASSWORD_FILE")).read()
databaseEnv = open(os.getenv("MARIADB_DATABASE_FILE")).read()


engine = create_engine(f"mysql+pymysql://{userEnv}:{passwordEnv}@db/{databaseEnv}", echo=True, future=True)



    