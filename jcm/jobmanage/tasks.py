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


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)