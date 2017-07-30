
from django import forms
from models import usermode,PostModel,LikeModel

class signupform(forms.ModelForm):
    class Meta:
        model = usermode
        fields = ['username','name','email','password']
class loginform(forms.ModelForm):
    class Meta:
        model=usermode
        fields=['username','password']
class PostForm(forms.ModelForm):
    model=PostModel
    fields=['image','caption']
class LikeForm(forms.ModelForm):
    class Meta:
        model=LikeModel
        fields=['post']
