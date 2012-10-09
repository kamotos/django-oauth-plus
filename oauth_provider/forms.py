from django import forms
from models import Consumer, Token

class AuthorizeRequestTokenForm(forms.Form):
    oauth_token = forms.CharField(widget=forms.HiddenInput)
    authorize_access = forms.BooleanField(required=False)


class DeauthorizeConsumer(forms.Form):
    application = forms.ModelChoiceField(queryset=Consumer.objects.all())


    def delete(self, user_id):
        consumer =  self.cleaned_data['application']
        Token.objects.filter(user=user_id, consumer=consumer).delete()
