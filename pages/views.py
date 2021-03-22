from django.shortcuts import render
from .models import Team
from cars.models import Car
# Create your views here.
# creating funciton. view are requested by browser render-> throwing to some other page

def home(request):
    #get all modal objects..
    teams = Team.objects.all()
    #get all cars and filter it

    featured_cars = Car.objects.order_by('created_date').filter(is_featured = True)
    all_cars = Car.objects.order_by('created_date')

    #search_fields = Car.objects.values('model','state','year')
    #to seacrch unique fields

    model_search = Car.objects.values_list('model',flat = True).distinct()
    year_search = Car.objects.values_list('year',flat = True).distinct()
    state_search = Car.objects.values_list('state',flat = True).distinct()

    data = {
   'teams':teams,#store it in teams
   'featured_cars':featured_cars,
   'all_cars':all_cars,
  # 'search_fields':search_fields,
    'state_search':state_search,
    'year_search':year_search,
    'model_search':model_search,


    }
    return render(request,'pages/home.html',data)#pass it to front end

def about(request):
    #get all modal objects..
    teams = Team.objects.all()
    data = {
   'teams':teams,#store it in teams
    }
    return render(request,'pages/about.html',data)

def services(request):
    return render(request,'pages/services.html')

def contact(request):
    return render(request,'pages/contact.html')
