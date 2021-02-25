from django.urls import path
from . import views

#127../cars

urlpatterns = [
path('',views.cars,name='cars'),
]
