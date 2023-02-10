from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.mail import EmailMessage
import random
import time

from other.constants import EMAIL_TASK_PRIORITY

logger = get_task_logger(__name__)


# Sending message with Token to User email
@shared_task(name='activate_user', priority=EMAIL_TASK_PRIORITY)
def activate_user(data):
    logger.info('EMAIL START TO SEND')
    is_task_completed = False
    try:
        is_task_completed = True
    except Exception as ex:
        logger.error(str(ex))
    if is_task_completed:
        email = EmailMessage(subject=data['email_subject'], body=data['email_body'], to=[data['receivers']])
        email.send()
    print('email has sent')
    return f'Email has send to {data["receivers"]}'


@shared_task(name='reset_password', priority=EMAIL_TASK_PRIORITY)
def reset_password(data):
    pass
