from itertools import product
from lib2to3.fixes.fix_input import context

import razorpay
from django.contrib.auth.views import LoginView
from django.shortcuts import render,redirect
from cart.forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView

from shop.models import Product
from cart.models import Cart,OrderDetails,Payment,OrderDetails

from shop.models import Category


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # user = form.save()  # Save the user instance
            # login(request, user)  # Automatically log in the user
            return redirect('shop:home')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})


class Login(LoginView):
    template_name = 'login.html'


@login_required()
def user_logout(request):
    logout(request)
    return redirect('cart:login')

@login_required()
def addtocart(request,i):
    u = request.user
    p = Product.objects.get(id=i)

    try:
        c = Cart.objects.get(user=u, product=p)
        if(p.stock>0):
            c.quantity+=1
            c.save()
            p.stock -=1
            p.save()
    except:
        c = Cart.objects.create(user=u, product=p, quantity=1)
        if(p.stock>0):
            c.save()
            p.stock -= 1
            p.save()
    return redirect('cart:cartview')

@login_required()
def cartview(request):
    u = request.user
    c =  Cart.objects.filter(user=u)

    #calculate sub total
    total = 0
    for i in c:
        total +=  i.quantity*i.product.price
    sub_total = total + 45
    context = {'cart':c, 'total':total, 'sub_total':sub_total}
    return render(request,'cart.html',context)

def cart_decrement(request,i):
    p = Product.objects.get(id=i)
    u = request.user
    try:
        cart = Cart.objects.get(user=u, product=p)
        if(cart.quantity > 1):
            cart.quantity -= 1
            cart.save()
            p.stock += 1
            p.save()
        else:
            cart.delete()
            p.stock += 1
            p.save()
    except:
        pass
    return redirect('cart:cartview')

def delete_cart_item(request,i):
    p = Product.objects.get(id=i)
    u = request.user
    try:
        cart = Cart.objects.get(user=u, product=p)
        cart.delete()
        p.stock += cart.quantity
        p.save()
    except:
        pass
    return redirect('cart:cartview')

class AddCategory(CreateView):
    template_name = 'add_category.html'
    model = Category
    fields = ['name','image','description']
    success_url = reverse_lazy('shop:home')

class AddProduct(CreateView):
    template_name = 'add_product.html'
    model = Product
    fields = ['name','image','description','price','stock','category']
    success_url = reverse_lazy('shop:home')


class AddStock(UpdateView):
    template_name = 'add_stock.html'
    model = Product
    fields = ['stock']
    # success_url = reverse_lazy('shop:home')
    def get_success_url(self):
        return  reverse_lazy('shop:productInfo',kwargs={'pk':self.object.id})

def billingDetails(request):
    if(request.method == 'POST'):
        #Read input from the form fields
        a = request.POST['a']
        ph = request.POST['p']
        pin = request.POST['pin']

        # calculate total bill amount
        u = request.user
        c = Cart.objects.filter(user=u)
        total = 0
        for i in c:
            total += i.quantity * i.product.price
        print(total)

        # Razorpay client connection
        client = razorpay.Client(auth=('rzp_test_bBwWlb8qCRcLtH','iStsCqLEfhmZSIdzbp34Beim'))

        # Razorpay order creation
        response_payment = client.order.create(dict(amount=int(total * 100), currency='INR'))
        print(response_payment)

        # retrieve the order ID from response
        order_id = response_payment['id']

        # retrieve the status from response
        status = response_payment['status']

        if(status=='created'):
            p = Payment.objects.create(name=u.username,amount=total,order_id=order_id)
            p.save()

            for i in c:
                o = OrderDetails.objects.create(product=i.product,user=i.user,phone=ph,address=a,pin=pin,order_id=order_id,no_of_items=i.quantity)
            context = {'payment':response_payment,'name':u.username}
            return render(request,'payment.html',context)



    return render(request,'billing_details.html')


from django.contrib.auth.models import User
from django.contrib.auth import login
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

        o = OrderDetails.objects.filter(order_id=response['razorpay_order_id'])
        for i in o:
            i.payment_status = "completed"
            i.save()

        c = Cart.objects.filter(user=user)
        c.delete()

    except:
        pass

    return render(request,'payment_status.html')


def myOrders(request):
    u = request.user
    o = OrderDetails.objects.filter(user=u,payment_status="completed")
    context = {'orders':o}
    return render(request,'my_orders.html',context)