"""
URL configuration for crms project.

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

from cars import views

app_name = 'cars'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view(),name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('addcar',views.AddCar.as_view(),name='addcar'),
    path('car_list',views.AllCars.as_view(),name='car_list'),
    path('car_details/<int:pk>',views.CarDetail.as_view(),name='car_details'),
    path('edit_car<int:pk>',views.edit_car,name='editcar'),
    path('delete/<int:pk>', views.DeleteCar.as_view(), name='delete_car'),
    path('manual_cars',views.ManualCars.as_view(),name='manual_cars'),
    path('automatic_cars',views.AutomaticCars.as_view(),name='automatic_cars'),
    path('addreview',views.AddReview.as_view(),name='add_review'),
]


from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
