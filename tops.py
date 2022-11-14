from datetime import datetime
#In order to run the script asynchronously so it triggers tops in time we use a BlockingScheduler
# This means no other processing at the same time
from apscheduler.schedulers.blocking import BlockingScheduler
# To use pygame libraries for RaspberryPi:
import pygame
# To use a cmd tool as mpg123, should work in other hardware if you don't have a RaspberryPi:
import os
# We're going to use 3 types of Triggers
from apscheduler.triggers.combining import AndTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger

pygame.mixer.init()
pygame.mixer.music.load("tops.wav")
pygame.mixer.music.set_volume(1.0)

# This is the triggering function
def tops_job():
    pygame.mixer.music.play()
    # If you prefer an cmd call instead...
    # os.system('mpg123 tops.mp3 &')
    print("Tops triggered at: ", datetime.now())

# Here we are defining our scheduler as a blocking one
scheduler = BlockingScheduler()

# Time resolution is done a second level, not milisecons. 
# So you have to adjust the wav/mp3 file to sync it with the realtime seconds. In my Raspberry Pi 4, it takes about 20ms to trigger
# so I play the wav file at 54 seconds so the first top is at second 55. I compensate all this in the sound file.

# This line triggers the tops each hour from start_date. This are the well known "every-hour-tops". Is an "INTERVAL" type trigger
scheduler.add_job(tops_job, 'interval', hours=1, start_date='2021-04-11 23:59:54')

# This ones trigger tops at specified time and weekdays. It's a "CRON" type trigger
scheduler.add_job(tops_job, 'cron', hour=6, minute=29, second=54, day_of_week='mon-fri')
scheduler.add_job(tops_job, 'cron', hour=7, minute=29, second=54, day_of_week='mon-fri')
scheduler.add_job(tops_job, 'cron', hour=8, minute=29, second=54, day_of_week='sat-sun')
scheduler.add_job(tops_job, 'cron', hour=14, minute=29, second=54, day_of_week='mon-sun')

# With all the different jobs assigned, now it's time to run the script. 
# After this, the thread is assigned to the scheduler exclusively, forget about running anything else in this script.
scheduler.start()
