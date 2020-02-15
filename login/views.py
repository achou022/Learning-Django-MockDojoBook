from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def login(request):
    return render(request, "login.html")

def success(request):
    if 'user' in request.session:
        return render(request, 'welcome.html')
    else:
        return redirect('/wall')

def register(request):
    errors=User.objects.validator(request.POST)
    if(len(errors)>0):
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/')
    else:
        newUser=User.objects.create(firstName=request.POST['firstName'],lastName=request.POST['lastName'],email=request.POST['email'],pw=bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()).decode())
        request.session['user']=newUser.id
        # request.session set to logged in user and see if i can access object values in jinja
        return redirect('/wall')

def loginValidation(request):
    errors=User.objects.validator(request.POST)
    if(len(errors)>0):
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/')
    else:
        user=User.objects.filter(email=request.POST['email'])
        if user:
            loggedUser=user[0]
            if bcrypt.checkpw(request.POST['pw'].encode(), loggedUser.pw.encode()):
                request.session['user']=loggedUser.id
                return redirect('/wall')
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')