from django.shortcuts import render,redirect
from .models import BrandLogos, NewCar,UsedCar,RentCar
from .forms import UsedCarsForm
# Create your views here.
def home(request):
    cars={
        'Ucars':UsedCar.objects.all(),
        'Ncars':NewCar.objects.all(),
    }
    return render(request,'pages/home.html',cars)

def newcars(request):
    search=NewCar.objects.all()
    title=None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(ad_title__icontains=title)
    context={
        'Ncars':search
    }
    return render(request,'pages/newcars.html',context)

def newcar(request,id):
    car_id = NewCar.objects.get(id=id)
    context={
        'Newcar':car_id
    }
    return render(request,'pages/singlenewcar.html',context)

def usedcars(request):
    search=UsedCar.objects.all()
    title=None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(ad_title__icontains=title)
    context={
        'Ucars':search
    }
    return render(request,'pages/usedcars.html',context)

def usedcar(request,id):
    car_id = UsedCar.objects.get(id=id)
    context={
        'Usedcar':car_id
    }
    return render(request,'pages/singleusedcar.html',context)

def sell(request):
    context = {
        'usedcars':UsedCar.objects.all(),
        'form':UsedCarsForm()
    }
    if request.method == 'POST':
        UsedCarsData=UsedCarsForm(request.POST,request.FILES)
        if UsedCarsData.is_valid():
            UsedCarsData.save()
            return redirect('usedcars')
    return render(request,'pages/sellyourcar.html', context)

def rentcars(request):
    search=RentCar.objects.all()
    title=None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(ad_title__icontains=title)
    context={
        'Rcars':search
    }
    return render(request,'pages/rentcars.html',context)

def rentcar(request,id):
    car_id = RentCar.objects.get(id=id)
    context={
        'Rentcar':car_id
    }
    return render(request,'pages/singlerent.html',context)