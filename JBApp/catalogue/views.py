from django.shortcuts import render
from django.http import HttpResponse
from .models import Tee, Exclusive_Apparel, Pant, Hoodies_Sweater


# Create your views here.

def cat1(request):
    tees = Tee.objects.all()
    return render(request, 'catalogue/teecatalogue.html', {'tees': tees})


def cat2(request):
    hoodies_sweaters = Hoodies_Sweater.objects.all()
    return render(request, 'catalogue/hoodiescatalogue.html', {'hoodies_sweaters': hoodies_sweaters})


def cat3(request):
    pants = Pant.objects.all()
    return render(request, 'catalogue/pantscatalogue.html', {'pants': pants})


def cat4(request):
    exclusive_apparel = Exclusive_Apparel.objects.all()
    return render(request, 'catalogue/exclusivecatalogue.html', {'exclusive_apparel': exclusive_apparel})