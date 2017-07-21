
from django import forms
from models import usermod

class signupform(forms.ModelForm):
    class Meta:
        model = usermod
        fields = ['user_name','full_name','email','password']

