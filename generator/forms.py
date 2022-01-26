from django.core import validators
from django import forms
from .models import SendMail

class UserSendMail(forms.ModelForm):
    class Meta:
        model = SendMail
        fields = ['subject', 'useremail', 'message']
        widgets = {
            'subject': forms.TextInput(attrs={'placeholder': 'Write your Subject','class':'input-subject'}),
            'useremail': forms.EmailInput(attrs={'placeholder': 'Write your Mail ID','class':'input-to'}),
            'message': forms.Textarea(attrs={'placeholder': 'Write your Mail ID','class':'input-message'})
        }