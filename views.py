from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Destination
from django.contrib.auth.models import User,auth


# Create your views here.
def index(request):
    if request.method =='POST':
        username= request.POST['name']
        email= request.POST['email']
        password1= request.POST['password1']
        password2= request.POST['password2']

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        print('user created')
        return redirect('tlogin/autovi.html')
    else:
        return render(request,'index.html')