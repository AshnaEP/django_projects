from django.shortcuts import render
from django.shortcuts import render,redirect
from cars.models import Car
from booking.models import CarBooking,Payment
from django.views.generic import ListView, DetailView, UpdateView,DeleteView
from django.urls import reverse_lazy
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import login


# Create your views here.
def bookCar(request,i):
    u = request.user
    c = Car.objects.get(id=i)
    if (request.method == 'POST'):
        name=request.POST['n']
        email=request.POST['e']
        ph=request.POST['p']
        p_location=request.POST['pl']
        p_date=request.POST['p_date']
        p_time=request.POST['p_time']
        days=request.POST['n_days']
        d_location=request.POST['dl']
        d_date=request.POST['d_date']
        d_time=request.POST['d_time']
        # c_booking=CarBooking.objects.create(car=c,user=u,name=name,email=email,phone=ph,
        #     pick_up_location=p_location,pick_up_date=p_date,pick_up_time=p_time,num_of_days=days,
        #     drop_off_location=d_location,drop_off_date=d_date,drop_off_time=d_time)
        # c_booking.save()
        # return redirect('booking:my_bookings')
        # Razorpay client connection
        client = razorpay.Client(auth=('rzp_test_bBwWlb8qCRcLtH', 'iStsCqLEfhmZSIdzbp34Beim'))

        # Razorpay order creation
        total=100
        response_payment = client.order.create(dict(amount=int(total * 100), currency='AED'))
        print(response_payment)

        # retrieve the order ID from response
        order_id = response_payment['id']

        # retrieve the status from response
        status = response_payment['status']
        print('***************************************')
        print(status)
        if (status == 'created'):
            p = Payment.objects.create(name=u.username, amount=total, order_id=order_id)
            p.save()

            c_booking = CarBooking.objects.create(car=c, user=u, name=name, email=email, phone=ph,
              pick_up_location=p_location, pick_up_date=p_date, pick_up_time=p_time,
              num_of_days=days,drop_off_location=d_location, drop_off_date=d_date,
              drop_off_time=d_time,booking_id=order_id)
            c_booking.save()
            context = {'payment': response_payment, 'name': u.username}
            return render(request, 'payment.html', context)
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
        print(status)

    return render(request,'book_car.html')


@csrf_exempt
def paymentStatus(request,p):
    user = User.objects.get(username = p)
    login(request,user)

    response = request.POST
    print(response)

    # To check the validity (authenticity) of razorpay payment details received by application
    param_dict = {
        'razorpay_order_id':response['razorpay_order_id'],
        'razorpay_payment_id':response['razorpay_payment_id'],
        'razorpay_signature':response['razorpay_signature']
    }
    client = razorpay.Client(auth=('rzp_test_bBwWlb8qCRcLtH', 'iStsCqLEfhmZSIdzbp34Beim'))
    try:
        status = client.utility.verify_payment_signature(param_dict)
        print(status)
        pay = Payment.objects.get(order_id=response['razorpay_order_id'])
        pay.paid = True
        pay.razorpay_payment_id = response['razorpay_order_id']
        pay.save()

        book_ob = CarBooking.objects.get(booking_id=response['razorpay_order_id'])
        print(book_ob)
        book_ob.deposit_status = "completed"


        # book_ob =CarBooking.objects.filter(booking_id=response['razorpay_order_id']).update(deposit_status="completed")

        book_ob.save()

    except:
        pass

    return render(request,'payment_status.html')


def myBooking(request):
    u = request.user
    b=CarBooking.objects.filter(user=u,deposit_status='completed')
    context = {'booking': b}
    return render(request, 'my_bookings.html', context)


class MyBookingDetails(DetailView):
    model = CarBooking
    context_object_name = 'booked'
    template_name = 'my_booking_details.html'


class AllBookings(ListView):
    model = CarBooking
    context_object_name = 'booking'
    template_name = 'admin_booking_view.html'


class UpdateBooking(UpdateView):
    template_name = 'update_booking.html'
    model = CarBooking
    context_object_name = 'b'
    fields = ['name','email','phone','pick_up_location','pick_up_date','pick_up_time',
              'num_of_days','drop_off_location','drop_off_date','drop_off_time'
              ]

    def get_success_url(self):
        return reverse_lazy('booking:my_booking_details', kwargs={'pk': self.object.pk})

class CancelBooking(DeleteView):
    template_name = 'cancel_booking.html'
    model = CarBooking
    success_url = reverse_lazy('booking:my_bookings')