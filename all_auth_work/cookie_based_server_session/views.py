from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)  # creates session & sets cookie
            return redirect('dashboard')
        else:
            return render(request, 'cookie_based_server_session/login.html', {'error': 'Invalid credentials'})
    return render(request, 'cookie_based_server_session/login.html')


@login_required
def dashboard(request):
    return render(request, 'cookie_based_server_session/dashboard.html', {'user': request.user})


def logout_view(request):
    logout(request)  # clears session & cookie
    return redirect('login')
