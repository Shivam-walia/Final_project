# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from datetime import datetime
from myapp.forms import signupform
from myapp.forms import loginform
from django.contrib.auth.hashers import make_password,check_password
from myapp.models import usermode,sessiontoken
# Create your views here.
def signup_view(request):
    if request.method=='GET':
        #Display signup form       
         signup_form=signupform()
         template_name='signup.html'
    elif request.method=='POST':
        #process the form data
        signup_form=signupform(request.POST)
        #Validate form data
        if signup_form.is_valid():
            #validation successful
            username=signup_form.cleaned_data['username']
            name=signup_form.cleaned_data['name']
            email=signup_form.cleaned_data['email']
            password=signup_form.cleaned_data['password']
            #save to db
            new_user=usermode(name=name,username=username,password=make_password(password),email=email)
            new_user.save()
            return redirect("/login/")

          #  template_name='success.html'

    return render(request,template_name,{'signup_form':signupform})


#login form
def login_view(request):
    response_data={}
    if request.method=="GET":
        #display login form
        login_form=loginform()
        #template_name='login.html'
    
    elif request.method=="POST":
        login_form=loginform(request.POST)
        if login_form.is_valid():
            #validation checks
            username=login_form.cleaned_data['username']
            password=login_form.cleaned_data['password']
            #fetch data from db
            user=usermode.objects.filter(username=username).first()
            if user:
                #password compare
                if check_password(password,user.password):
                    #login sucessfully
                    new_token=sessiontoken(user=user)
                    new_token.create_token()
                    new_token.save()
                    response=redirect('/feed/')
                    response.set_cookie(key='session_token',value=new_token.session_token)
                    return response
                    
                   # template_name='login_success.html'
                else:
                    #Does not login
                #    template_name='login_fail.html'
                    response_data['message'] = 'Incorrect password  ..! Please try again...'
        
    response_data['login_form']=loginform

    return render(request,'login.html',response_data)

    #        else:
                #user do not exists
     #           template_name='login_fail.html'
      #  else:
       #     print"validation failed"
        #    template_name='login_fail.html'

        
    #return render(request,template_name,{'login_form':login_form})

def check_validation(request):
    if request.COOKIES.get('session_token'):
        session=sessiontoken.objects.filter(session_token=request.COOKIES.get('session_token')).first()
        if session:
            return session_user
        else:
            return None



