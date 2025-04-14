from django.contrib.auth.models import User
from django.contrib.auth.views import UserModel
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import get_user_model


# Create your views here.
# class SignUp(CreateView):
#     template_name = 'register.html'
#     model = UserModel
#     form_class = UserRegistrationForm
#     success_url = reverse_lazy('home')

def signup(request):
    if(request.method=='POST'):
        f=request.POST['f']
        l=request.POST['l']
        u=request.POST['u']
        e=request.POST['e']
        p=request.POST['p']
        cp=request.POST['cp']
        if User.objects.filter(email=e).exists():
            messages.error(request, "This Email is already registered")
            return render(request, 'register.html')
        elif p==cp:
            user=User.objects.create_user(username=u,email=e,password=p,first_name=f,last_name=l)
            user.save()
            login(request, user)
            return redirect('cars:home')
        else:
            messages.error(request, "Passwords do not match.")
            return render(request, 'register.html')
    return render(request,'register.html')

class UserLogin(LoginView):
    template_name = 'login.html'

    def form_invalid(self, form):
        """Called when the form is invalid (login fails)"""
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        if not username or not password:
            messages.error(self.request, "Both username and password are required.")
        else:
            # Check if the user exists
            user = get_user_model().objects.filter(username=username).first()
            if not user:
                messages.error(self.request, "Username does not exist.")
            else:
                # Check if the password is incorrect
                messages.error(self.request, "Incorrect password.")

        return super().form_invalid(form)

@login_required()
def user_logout(request):
    logout(request)
    return redirect('user:login')


