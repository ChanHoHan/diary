from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):

    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('contents')
        else:
            return render(request, 'home.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            User.objects.create_user(username = request.POST['username'], password=request.POST['password1'])
            return redirect('home')
    return render(request, 'signup.html')


