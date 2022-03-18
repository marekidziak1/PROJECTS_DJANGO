from django import forms
from . models import Participant

class RegistrationForm(forms.Form):
    email = forms.EmailField(label = 'Your email')
'''
class RegistrationForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Participant
        fields = ['email']'''