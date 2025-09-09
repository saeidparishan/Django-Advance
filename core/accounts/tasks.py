from celery import shared_task
from time import sleep

@shared_task
def sendEmail():
    sleep(3)
    print('<h1>done sending</h1>')