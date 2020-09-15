from django import forms
from django.core.mail import send_mail


class EmailForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.widgets.Textarea)

    def send_email(self):
        body = self.cleaned_data['message']
        send_mail(
            'Hello from demo',
            body,
            'from@me.com',
            ['to@you.com'],
            fail_silently=False,
        )
        