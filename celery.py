from __future__ import absolute_import
from celery import Celery

app = Celery('celery_rabbitm',
             broker='amqp://jimmy:jimmy123@localhost/jimmy_vhost',
             backend='rpc://',
             include=['celery_rabbitm.tasks'])