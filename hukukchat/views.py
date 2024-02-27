from django.shortcuts import render
from django.shortcuts import render

def open_page(request):
    return render(request, 'open.html')

def login_page(request):
    return render(request, 'login.html')

def register_page(request):
    return render(request, 'sing_in.html')

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'sing_in.html', {'form': form})
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            return redirect('index')
        else:
            
            pass
    return render(request, 'login.html')
