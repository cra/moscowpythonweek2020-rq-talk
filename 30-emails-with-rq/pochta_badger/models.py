from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from markdown import markdown as md

from pochta_badger.mail_tools import slow_mail_send
from rq import Queue
from redis import Redis


class Campaign(models.Model):
    message = models.TextField(help_text='markdown supported')
    message_rendered = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.message_rendered = md(self.message)
        super().save(*args, **kwargs)

        queue = Queue(connection=Redis())
        queue.enqueue(slow_mail_send, self)