from django.urls import path
from . import views

#127../cars

urlpatterns = [
path('login',views.login,name='login'),
path('logout',views.logout,name='logout'),
path('register',views.register,name='register'),
path('dashboard',views.dashboard,name='dashboard'),

]
