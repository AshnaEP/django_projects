from lib2to3.fixes.fix_input import context

from django.shortcuts import render,redirect
from books.models import Book
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request,'home.html')

@login_required()
def add_books(request):
    if(request.method == "POST"):

        #Normal form fields
        tit = request.POST['t']
        aut = request.POST['a']
        pri = request.POST['p']
        lan = request.POST['l']
        page = request.POST['pgs']

        #File uploads
        img=request.FILES['i']
        pdf=request.FILES['pdf']
        b = Book.objects.create(title=tit, author=aut, price=pri, language=lan, pages=page,image=img,pdf=pdf)
        b.save()
        return redirect('books:view')
    return render(request,'add.html')


@login_required()
def view_books(request):
    b=Book.objects.all()
    context={'book':b}
    return render(request,'view.html',context)


@login_required()
def factorial(request):
    if(request.method == "POST"):
        num = request.POST['n']
        facto=1
        for i in range(1,int(num)+1):
            facto = facto * i
        return render(request,'factorial.html',{'fact':facto})
    return render(request,'factorial.html')


@login_required()
def view_details(request, i):
    b=Book.objects.get(id=i)
    context={'book':b}
    return render(request,'view_details.html',context)


@login_required()
def delete_book(request, i):
    b= Book.objects.get(id=i)
    b.delete()
    return redirect('books:view')


@login_required()
def edit_book(request,i):
    b=Book.objects.get(id=i)
    if(request.method == 'POST'):
        b.title = request.POST['t']
        b.author = request.POST['a']
        b.price = request.POST['p']
        b.language = request.POST['l']
        b.pages = request.POST['pgs']

        if(request.FILES.get('im') == None):
            b.save()
        else:
            b.image = request.FILES.get('im')

        if (request.FILES.get('pdf') == None):
            b.save()
        else:
            b.pdf = request.FILES.get('pdf')
        b.save()
        return redirect('books:view')
    context={'book':b}
    return render(request,'edit_book.html',context)


def search(request):
    if(request.method == 'POST'):
        query = request.POST['q']
        b = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
        context = {'book':b}
    return render(request,'search.html',context)