from django.contrib import admin
from django.urls import path
from . import views

#127../about page. view.about (is the fn)

urlpatterns = [
path('',views.home,name='home'),
path('about',views.about,name='about'),
path('services',views.services,name='services'),
path('contact',views.contact,name='contact'),
]
