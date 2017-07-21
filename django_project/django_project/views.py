# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from datetime import datetime
from myapp.forms import signupform
# Create your views here.
def signup_view(request):
    today=datetime.now
    signup_form=signupform()
    return render(request,'signup.html',{'today':today},{'signup_form':signup_form})
