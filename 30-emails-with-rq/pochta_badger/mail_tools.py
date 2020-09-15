import time 

from django.core.mail import send_mail

def slow_mail_send(email):
    time.sleep(3)
    print(f'Got email with {email.message}')
    send_mail(
        'Hello from demo',
        email.message,
        'from@me.com',
        ['to@you.com'],
        fail_silently=False,
        html_message=email.message_rendered,
    )