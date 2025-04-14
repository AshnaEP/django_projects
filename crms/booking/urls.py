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

from booking import views

app_name = 'booking'

urlpatterns = [
    path('bookcar/<int:i>',views.bookCar,name='bookcar'),
    path('my_bookings',views.myBooking,name='my_bookings'),
    path('my_booking_details/<int:pk>',views.MyBookingDetails.as_view(),name='my_booking_details'),
    path('all_bookings',views.AllBookings.as_view(),name='all_bookings'),
    path('update_booking/<int:pk>',views.UpdateBooking.as_view(),name='update_booking'),
    path('cancel/<int:pk>', views.CancelBooking.as_view(), name='cancel-booking'),
    path('payment_status/<str:p>',views.paymentStatus,name='payment_status'),
]


from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
