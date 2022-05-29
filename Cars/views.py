from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import UsedCarsForm
# Create your views here.

#HOME PAGE
def home(request):
    cars={
        'Ucars':UsedCar.objects.all(),
        'Ncars':NewCar.objects.all(),
        'Rcars':RentCar.objects.all()
    }
    return render(request,'pages/home.html',cars)

#New Car Pages(list-single car)
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

#Used Car Pages(list-single car)
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

#Sell form
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

#Rental Car Pages(list-single car)
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

#Update used car
def update(request,id):
    car_id = UsedCar.objects.get(id=id)
    if request.method == 'POST':
        UsedCarsData=UsedCarsForm(request.POST,request.FILES,instance=car_id)
        if UsedCarsData.is_valid():
            UsedCarsData.save()
            return redirect('usedcars')
    else:
        UsedCarsData = UsedCarsForm(instance=car_id)
    context={
        'form':UsedCarsData,
    }
    return render(request,'pages/updateusedcar.html',context)

#Delete used car
def delete(request,id):
    usedcar_delete = get_object_or_404(UsedCar, id=id)
    if request.method == 'POST':
        usedcar_delete.delete()
        return redirect('/')
    return render(request,'pages/deleteusedcar.html')

#Footer links 
def footer(request):
    return render(request,'pages/footerLinks.html')