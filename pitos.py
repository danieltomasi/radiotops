from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import pygame
import os
from apscheduler.triggers.combining import AndTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger

pygame.mixer.init()
pygame.mixer.music.load("horarias2021.wav")
pygame.mixer.music.set_volume(1.0)

# Definir la función a ejecutar
def pitos_job():
    pygame.mixer.music.play()
    #os.system('mpg123 horarias2021.mp3 &')
    print("Ejecutado pitos: ", datetime.now())
    
def imprimir_mensaje():
    print("Función ejecutada a las: ", datetime.now())

# Asigar un programador bloqueante
scheduler = BlockingScheduler()

# Store the job in a variable in case we want to cancel it. No coge milisegundos, lo compenso en el mp3. Calculo con los
# relojes aproximadamente unos 20ms lo que tarda en reproducir
scheduler.add_job(pitos_job, 'interval', hours=1, start_date='2021-04-11 23:59:54')
scheduler.add_job(pitos_job, 'cron', hour=6, minute=29, second=54, day_of_week='mon-fri')
scheduler.add_job(pitos_job, 'cron', hour=7, minute=29, second=54, day_of_week='mon-fri')
scheduler.add_job(pitos_job, 'cron', hour=8, minute=29, second=54, day_of_week='mon-sun')
scheduler.add_job(pitos_job, 'interval', hours=24, start_date='2021-04-11 14:29:54')

#Arrancar el programador. Con la función bloqueante, si hubiera mas cosas, este proceso se quedaría con el hilo para el solo
scheduler.start()
