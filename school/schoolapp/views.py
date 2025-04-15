from msilib.schema import ListView

from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, View

from schoolapp.models import School, Student
from django.contrib.auth.models import User

from schoolapp.forms import SchoolForm

from django.contrib.auth import logout


# Create your views here.
#class base view
class Home(TemplateView):
    template_name = 'home.html'


class AddSchool(CreateView):
    template_name = 'add_school.html'
    model = School
    # fields = ['name','principal','location']
    form_class = SchoolForm
    success_url = reverse_lazy('home')


class AddStudent(CreateView):
    template_name = 'add_student.html'
    model = Student
    fields = ['name','age','school']
    success_url = reverse_lazy('home')


class SchoolList(ListView):
    model = School
    template_name = 'school_list.html'
    context_object_name = 'sc'


class SchoolDetails(DetailView):
    model = School
    template_name = 'school_details.html'
    context_object_name = 'sc'


class StudentList(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'st'

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     queryset = qs.filter(school__location="EKM")
    #     return queryset

    # def get_queryset(self):
    #       qs = super().get_queryset()
    #       queryset = qs.filter(name__icontains="nu")
    #       return queryset

    # def get_queryset(self):
    #       qs = super().get_queryset()
    #       queryset = qs.filter(age__gt=14)
    #       return queryset

    # def get_queryset(self):
    #       qs = super().get_queryset()
    #       queryset = qs.filter(age__lt=16)
    #       return queryset

    def get_queryset(self):
          qs = super().get_queryset()
          queryset = qs.filter(name__startswith='A')
          return queryset

    def get_context_data(self):
        context =  super().get_context_data()
        context['name']=['Priya']
        context['school'] = School.objects.all()
        return context


class Register(CreateView):
    model = User
    fields = ['username','password','email','first_name','last_name']
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        u = form.cleaned_data['username']
        p = form.cleaned_data['password']
        e = form.cleaned_data['email']
        f = form.cleaned_data['first_name']
        l = form.cleaned_data['last_name']

        u = User.objects.create_user(username=u,password=p,email=e,first_name=f, last_name=l)
        u.save()
        return redirect('home')


class Login(LoginView):
    template_name = 'login.html'


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')