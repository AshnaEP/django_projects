from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from users.models import CustomUser


# Create your views here.
def register(request):
    if(request.method == 'POST'):
        u_name = request.POST['u']
        p = request.POST['p']
        c = request.POST['c']
        e = request.POST['e']
        f = request.POST['e']
        l = request.POST['l']
        n = request.POST['ph']
        a = request.POST['a']

        if(p==c):
            # u = User.objects.create(username=u_name, password=p, email=e, first_name = f, last_name = l)
            u = CustomUser.objects.create_user(username=u_name, password=p, email=e, first_name = f, last_name = l,phone = n, address = a)
            u.save()
            return redirect('books:home')

        else:
            messages.error(request,"Password are not same")
    return render(request,'register.html')

def user_login(request):
    if(request.method == 'POST'):
        u = request.POST['u']
        p = request.POST['p']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect('books:home')
        else:
            messages.error(request,"Invalid credentails")
    return render(request,'login.html')



@login_required()
def user_logout(request):
    logout(request)
    return redirect('users:login')
