from django.urls import path
from . import views

#127../about page. view.about (is the fn)

urlpatterns = [
path('inquiry',views.inquiry,name='inquiry'),
]
