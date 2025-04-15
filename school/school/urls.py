"""
URL configuration for school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from schoolapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view(),name="home"),
    path('add',views.AddSchool.as_view(),name="add"),
    path('addstudent',views.AddStudent.as_view(),name="addstudent"),
    path('viewSchool',views.SchoolList.as_view(),name="viewSchool"),
    path('schooldetails/<int:pk>',views.SchoolDetails.as_view(),name="schooldetails"),
    path('studentlist',views.StudentList.as_view(),name="studentlist"),
    path('register',views.Register.as_view(), name="register"),
    path('login',views.Login.as_view(), name="login"),
    path('logout',views.Logout.as_view(), name="logout"),
]
