from django.shortcuts import render

from django.views.generic import FormView, ListView 
from django.http.response import HttpResponse

from pochta_badger.forms import EmailForm


class SendEmailView(FormView):
    form_class = EmailForm
    template_name = 'send_email.html'
    success_url = '/list'

    def form_valid(self, form: EmailForm):
        form.send_email()
        return super().form_valid(form)


class DoneView(ListView):
    template_name = 'list_sent_emails.html'

    def get_queryset(self, *args, **kwargs):
        emails = [
            '''## Hello
_First email content_
            ''',
            '''
## Please respond

**Second email content**
'''
        ]
        return emails