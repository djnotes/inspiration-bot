import time
import math

from pyrogram.types import User


from apscheduler.schedulers.asyncio import AsyncIOScheduler

from pyrogram import Client,filters
import random

from pyrogram.types.bots_and_keyboards.reply_keyboard_markup import ReplyKeyboardMarkup


class Commands:
    twice_daily = "Send Inspiration Twice A Day"
    once_daily = "Send Inspiration Once A Day"
    once_weekly = "Send Inspiration Once A Week"
    stop_sending = "Stop Sending Inspirations 🛑"

class Messages:
    you_will_no_longer_receive_inspirations = "You will no longer receive inspirations."
    you_will_receive_twice_daily = "You will receive inspirations twice a day"
    you_will_receive_once_daily = "You will receive inspirations once a day"
    you_will_receive_once_weekly = "You will receive inspirations once a week"



app = Client("session/bot")



admin = 'djnotes'

audience_ids = ['djnotes']

# start_time = time.time()

def randomInspiration():
    phrases = [
        "Wake up and work",
        "Every second matters",
        "Today, you will go one step closer to your goal",
        "Wake up! Today is an important day",
        "Today is an awesome day and you are an awesome person!",
        "Let's make our dreams come true",
        
    ]

    return phrases[random.randint(0, phrases.__len__() - 1)]


async def job(user: User, start_time: int):
    if(app.is_initialized):
        lifetime = math.ceil(time.time() - start_time)
        if lifetime <= 3600:
            message = f"My age: {math.floor(lifetime)} seconds"
        elif  3600 <= lifetime and lifetime <= 86400:
            message = f"My age: {math.floor(lifetime / 3600)} hours"
        else:
            message = f"My age: {math.floor(lifetime / 86400)} days"
        await app.send_message(user.id, randomInspiration() +  f"\n{message}")
        # for id in audience_ids: 
            # await app.send_message(id, f"My age: {time.time() - start_time} seconds")



scheduler = AsyncIOScheduler()

def schedule(interval: int, user: User, start_time = time.time()):
    scheduler.add_job(func = job, trigger = "interval", args = (user, start_time) , seconds =  interval, id = f"{user.id}")
    app.send_message(admin, f"New subscription: {user}")


# scheduler.add_job(job, "interval", seconds = 10)

scheduler.start()

@app.on_message(filters.private)
async def handle_message(client, message):
    if message.text == "/start":
        await message.reply("Main Menu", reply_markup = ReplyKeyboardMarkup(keyboard = [
            [Commands.once_daily,],
            [Commands.twice_daily,],
            [Commands.once_weekly,],
            [Commands.stop_sending,],
        ]))

    elif message.text == Commands.twice_daily:
        # schedule(12 * 3600, message.from_user)
        schedule(10, message.from_user)
        await message.reply(Messages.you_will_receive_twice_daily)

    elif message.text == Commands.once_daily:
        schedule(24 * 3600, message.from_user)
        await message.reply(Messages.you_will_receive_once_daily)
    elif message.text == Commands.once_weekly:
        schedule(24 * 3600 * 3, message.from_user)
        await message.reply(Messages.you_will_receive_once_weekly)
    elif message.text == Commands.stop_sending:
        scheduler.remove_job(f"{message.from_user.id}") #Using user id as job id 
        await message.reply(Messages.you_will_no_longer_receive_inspirations)

app.run()



