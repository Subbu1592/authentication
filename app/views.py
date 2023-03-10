from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login_page')
def home(request):

    return render(request, 'home.html')

def login_page(request):
    if request.method=='POST':
        username= request.POST.get('username')
        pass1=request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('user is invalid.')


    return render(request,'login_page.html')


def sign_up(request):
    if request.method =='POST':
        username = request.POST.get('username')

        email = request.POST.get('email')

        pass1 = request.POST.get('password1')

        pass2 = request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse('wrong password')
        else:


        

            my_user=User.objects.create_user(username, email, pass1)
            my_user.save()
            return redirect('login_page')
    return render(request,'sign_up.html')


def logout_page(request):
    logout(request)
    return redirect('login_page')