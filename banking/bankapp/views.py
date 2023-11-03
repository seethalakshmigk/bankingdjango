from urllib import request

from .forms import ApplicationForm
from .models import User_Table
from .models import Application


from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def user_login(request):
    message = ""
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']
        try:

            User = User_Table.objects.get(username=username, password=password)
            request.session['user_id'] = User.id
            return redirect('bankapp:apply')


        except User_Table.DoesNotExist:
            msg = "login failed"
            return render(request, 'login.html', {'message': message})
    return render(request, 'login.html')


def home(request):
    return render(request,'home.html')

def register(request):
    message = ""
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]


        if User_Table.objects.filter(username=username).exists():
            message = "use another username"
            return render(request, 'signup.html', {'message': message})
        else:
            User = User_Table(username=username, password=password)
            User.save()
            return redirect('bankapp:login')

    return render(request, 'signup.html')


def apply(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bankapp:msg')
    else:
        form = ApplicationForm()

    return render(request, 'apply.html', {'form': form})

def success(request):
    return render(request,'application_success.html')


def user_logout(request):

    logout(request)
    return redirect('bankapp:home')