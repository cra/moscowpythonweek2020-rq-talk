from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from markdown import markdown as md


class Campaign(models.Model):
    message = models.TextField(help_text='markdown supported')
    message_rendered = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.message_rendered = md(self.message)
        super().save(*args, **kwargs)
        send_mail(
            'Hello from demo',
            self.message,
            'from@me.com',
            ['to@you.com'],
            fail_silently=False,
            html_message=self.message_rendered,
        )