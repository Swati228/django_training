from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth



# Create your views here.
def login(request):
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        #check for authentication where username = input & pass
        user = auth.authenticate(username=username , password=password)
        if user is not None :
            auth.login(request,user)
            messages.success(request,"You are now successfully login")
            return redirect('dashboard')
        else :
            messages.error(request ,'Invalid login')
            return redirect(login)

    return render(request,'accounts/login.html')

def register(request):
    if request.method == 'POST' :
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password :
            if User.objects.filter(username = username).exists():
                messages.error(request,"Username Already exist")
                return redirect('register')
            else :
               if User.objects.filter(email = email).exists():
                   messages.error(request,"Email Already Exist")
                   return redirect('register')
               else:
                   user = User.objects.create_user(first_name = firstname , last_name = lastname , email = email , username = username , password = password )
                   user.save()
                   messages.success(request, "You are register")
                   return redirect('login')
        else:
            messages.error(request,"Password not macth")
            return redirect('register')

        #messages.error(request,'this is error message')
        #return redirect('register')
    else:
        return render(request,'accounts/register.html')

def dashboard(request):
    return render(request,'accounts/dashboard.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,"You are successfully logout ")
        return redirect('login')
    return redirect('home') #tell it to go to home with urls.py of pages
