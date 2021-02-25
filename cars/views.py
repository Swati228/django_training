from django.shortcuts import render

# accept request from browser
def cars(request):
    return render(request,'cars/cars.html') #when request is comming content of html file is show in browsr
