# coding:utf-8
#
# from celery import task
# from celery.utils.log import get_task_logger
#
# from jobmanage.emails import send_feedback_email
#
# logger = get_task_logger(__name__)
#
#
# @task(name="send_feedback_email_task")
# def send_feedback_email_task(email, message):
#     """sends an email when feedback form is filled successfully"""
#     logger.info("Sent feedback email")
#     return send_feedback_email(email, message)


from __future__ import absolute_import
from celery import shared_task
from celery.task.schedules import crontab  
from celery.decorators import periodic_task  
from celery.utils.log import get_task_logger 


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


logger = get_task_logger(__name__)  
 
@periodic_task(  
    run_every=(crontab(minute='*/1')),  
    name="test_hello",  
    ignore_result=True  
)  
def test_hello():  
    """ 
    Saves latest image from Flickr 
    """  
    print('============hello---------------')
    logger.info("Saved image from Flickr")


@periodic_task(  
    run_every=(crontab(minute='*/1')),  
    name="test_hello1",  
    ignore_result=True  
)  
def test_hello1():  
    """ 
    Saves latest image from Flickr 
    """  
    print('============hello1111111---------------')
    logger.info("Saved image from Flickr")


@periodic_task(  
    run_every=(crontab(minute='*/1')),  
    name="test_hello2",  
    ignore_result=True  
)  
def test_hello2():  
    """ 
    Saves latest image from Flickr 
    """  
    print('============hello222222222222---------------')
    logger.info("Saved image from Flickr")