from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,DetailView,DeleteView
from cars.models import Car,Reviews

# Create your views here.

# def home(request):
#     return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


class AddCar(CreateView):
    model = Car
    template_name = 'add_cars.html'
    fields = ['name','color','description','rent','image','featured']
    success_url = reverse_lazy('cars:car_list')


class AllCars(ListView):
    model=Car
    context_object_name='c'
    template_name='car_list.html'


class CarDetail(DetailView):
    model = Car
    context_object_name = 'details'
    template_name = 'car_details.html'


def edit_car(request,pk):
    c=Car.objects.get(id=pk)
    if(request.method == 'POST'):
        c.name = request.POST['name']
        c.color = request.POST['color']
        c.description = request.POST['description']
        c.rent = request.POST['rent']
        c.featured=request.POST.get('featured') == 'on'

        if(request.FILES.get('image') == None):
            c.save()
        else:
            c.image = request.FILES.get('image')
        c.save()
        return redirect('cars:car_list')
    context={'car':c}
    return render(request,'update_car.html',context)


class DeleteCar(DeleteView):
    template_name = 'delete_car.html'
    model = Car
    success_url = reverse_lazy('cars:car_list')


class Home(ListView):
    model = Car
    context_object_name = 'fc'
    template_name = 'home.html'

    def get_queryset(self):
        qs = super().get_queryset()
        queryset=qs.filter(featured=True)
        print(queryset)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Reviews.objects.all()  # Fetch all reviews
        return context


class ManualCars(ListView):
    model = Car
    context_object_name = 'manual'
    template_name = 'manual_cars.html'

    def get_queryset(self):
        qs = super().get_queryset()
        queryset=qs.filter(car_type='Manual')
        return queryset

class AutomaticCars(ListView):
    model = Car
    context_object_name = 'automatic'
    template_name = 'automatic_cars.html'

    def get_queryset(self):
        qs = super().get_queryset()
        queryset=qs.filter(car_type='Automatic')
        return queryset

# def bookCar(request,i):
#     u = request.user
#     c = Car.objects.get(id=i)
#     if (request.method == 'POST'):
#         name=request.POST['n']
#         email=request.POST['e']
#         ph=request.POST['p']
#         p_location=request.POST['pl']
#         p_date=request.POST['p_date']
#         p_time=request.POST['p_time']
#         days=request.POST['n_days']
#         d_location=request.POST['dl']
#         d_date=request.POST['d_date']
#         d_time=request.POST['d_time']
#         c_booking=CarBooking.objects.create(car=c,user=u,name=name,email=email,phone=ph,
#             pick_up_location=p_location,pick_up_date=p_date,pick_up_time=p_time,num_of_days=days,
#             drop_off_location=d_location,drop_off_date=d_date,drop_off_time=d_time)
#         c_booking.save()
#         return redirect('cars:car_list')
#     return render(request,'book_car.html')

class AddReview(CreateView):
    model = Reviews
    template_name = 'contact.html'
    fields = ['user_name','user_email','review']
    success_url = reverse_lazy('cars:home')
