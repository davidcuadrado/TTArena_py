from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from .forms import CustomAuthenticationForm


def home(request):
    return render(request, "core/home.html")

def play(request):
    return render(request, "core/play.html")

def services(request):
    return render(request, "core/services.html")

def blog(request):
    return render(request, "core/blog.html")

def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")

def custom_login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                # Redirect to a success page - you can change 'home' to your desired page
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def custom_logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    # Redirect to a logged out page - you can change 'home' to your desired page
    return redirect('home')