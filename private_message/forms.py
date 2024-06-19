from django import forms
from .models import PrivateMessage

class MessageForm(forms.ModelForm):
    class Meta:
        model = PrivateMessage
        fields = ['recipient,' 'subject', 'body']