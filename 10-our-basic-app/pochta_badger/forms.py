from django import forms


class EmailForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.widgets.Textarea)

    def send_email(self):
        pass
        