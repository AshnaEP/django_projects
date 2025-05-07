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
    fields = ['car_type','name','color','description','rent','image','featured']
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


class AddReview(CreateView):
    model = Reviews
    template_name = 'contact.html'
    fields = ['user_name','user_email','review']
    success_url = reverse_lazy('cars:home')
