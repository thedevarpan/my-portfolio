from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def Account(request):
    return HttpResponse("Account")


def Signup(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if (password != confirm_password):
                return HttpResponse("Passwords are not same")
            
            
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                return HttpResponse("Account already exists")
            
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.is_active = False
                user.save()
                return redirect('/')
            except Exception as e:
                print(e) 

    except Exception as e:
        print(e)
    return render(request, 'account/signup.html')



def Login(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                return redirect("/")

    except Exception as e:
        print(e)

    return render(request, 'account/login.html')


@login_required
def Profile(request):
    user_data = request.user
    params = {'user_data': user_data}
    return render(request, 'account/profile.html', params)