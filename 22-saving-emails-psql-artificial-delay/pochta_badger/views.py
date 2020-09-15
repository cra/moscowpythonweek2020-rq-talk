from django.shortcuts import render

from django.views.generic import CreateView, ListView
from django.http.response import HttpResponse

from pochta_badger.models import Campaign


class CreateCampaignView(CreateView):
    model = Campaign
    fields = ['message']
    template_name = 'send_email.html'
    success_url = '/list'


class DoneView(ListView):
    template_name = 'list_sent_emails.html'

    def get_queryset(self, *args, **kwargs):
        emails = Campaign.objects.all()
        return emails