from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Contact
from django.core.mail import send_mail


# Create your views here.
def inquiry(request):
    if request.method == 'POST' :
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        #if user is login
        if request.user.is_authenticated:
            #get all record from contact table then filter it where car_id=car_id
            has_contacted = Contact.objects.all().filter(car_id=car_id,user_id=user_id)
            if has_contacted :
                messages.error(request,"You have already send inquire about this car . We will get to you")
                return redirect('/cars/'+car_id)
        #Contact is table name and inside that column name values..
        admin_info = User.objects.get(is_superuser = True)
        admin_email = admin_info.email

        contact = Contact(car_id =car_id,car_title=car_title,first_name=first_name,user_id=user_id,last_name=last_name,customer_need=customer_need,state=state,email=email,phone=phone,city=city,message=message)
        send_mail(
                'Car inquiry on website',
                'You have a new inquiry about for the car'+car_title+'.Login to your admin panel for more deatils',
                'bhagatswati1996@gmail.com',
                [admin_email],
                fail_silently=False,
        )



        contact.save() #save in db
        messages.success(request,"Your request has been submitted....")
        return redirect('/cars/'+car_id)
