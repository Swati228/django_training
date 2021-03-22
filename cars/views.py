from django.shortcuts import render , get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage , PageNotAnInteger,Paginator

# accept request from browser
def cars(request):
    cars = Car.objects.order_by('created_date')
    paginator = Paginator(cars ,4)
    page = request.GET.get('page')
    page_cars = paginator.get_page(page)
    model_search = Car.objects.values_list('model',flat = True).distinct()
    year_search = Car.objects.values_list('year',flat = True).distinct()
    state_search = Car.objects.values_list('state',flat = True).distinct()
    data={
    'cars':page_cars,
    'state_search':state_search,
    'year_search':year_search,
    'model_search':model_search,
    }

    return render(request,'cars/cars.html',data) #when request is comming content of html file is show in browsr

def car_detail(request,id):
    single_car = get_object_or_404(Car , pk = id) #if we hiting url if present then it willfetch from car class or give 404
    data ={
    'single_car':single_car,
    }
    return render(request,'cars/car_detail.html' , data)


def search(request):
    cars = Car.objects.order_by('created_date')

    model_search = Car.objects.values_list('model',flat = True).distinct()
    year_search = Car.objects.values_list('year',flat = True).distinct()
    state_search = Car.objects.values_list('state',flat = True).distinct()
    transmission_search = Car.objects.values_list('transmission',flat = True).distinct()
    condition_search = Car.objects.values_list('condition',flat =True).distinct()

    if 'keyword' in request.GET: #checking in url if it has name=keyword
        keyword = request.GET['keyword'] #get that keyword value para
        if keyword:
            cars = cars.filter(car_title__icontains = keyword) #if paricular search no case requires..


    if 'model' in request.GET: #checking in url if it has name=keyword
        model = request.GET['model'] #get that keyword value para
        if model:
            cars = cars.filter(model__iexact = model) #get exact text.

    if 'state' in request.GET: #checking in url if it has name=keyword
        state = request.GET['state'] #get that keyword value para
        if state:
            cars = cars.filter(state__iexact = state)


    if 'year' in request.GET: #checking in url if it has name=keyword
        year = request.GET['year'] #get that keyword value para
        if year:
            cars = cars.filter(year__iexact = year) #if paricular search no case requires..

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if 'max_price' :
            cars = cars.filter(price__gte = min_price,price__lte = max_price)



    data={
    'cars':cars,
    'state_search':state_search,
    'year_search':year_search,
    'model_search':model_search,
    'transmission_search':transmission_search,
    'condition_search':condition_search,
    }
    return render(request,'cars/search.html',data)
