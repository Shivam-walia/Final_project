
from django import forms
from models import usermode

class signupform(forms.ModelForm):
    class Meta:
        model = usermode
        fields = ['username','name','email','password']
class loginform(forms.ModelForm):
    class Meta:
        model=usermode
        fields=['username','password']
