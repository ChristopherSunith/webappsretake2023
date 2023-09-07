from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.hashers import make_password
from .models import User


def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        # Hash the password
        hashed_password = make_password(password)

        user = User(username=username, password=hashed_password, role=role)
        user.save()
        return redirect('register:login')

    return render(request, 'register/registration.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use authenticate to check the user's credentials
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Authentication successful, set the user's session
            auth_login(request, user)
            return redirect('register:dashboard')
        else:
            error_message = "Invalid username or password"
            return render(request, 'register/login.html', {'error_message': error_message})

    return render(request, 'register/login.html')


# def dashboard(request):
#     return render(request, 'register/dashboard.html')
def dashboard(request):
    # Check if the user is logged in and has a role
    if request.user.is_authenticated and request.user.role:
        role = request.user.role.lower()  # Get the role in lowercase for comparison

        # Redirect the user based on their role
        if role == 'administrator':
            return render(request, 'register/dashboard_admin.html')
        elif role == 'supervisor':
            return render(request, 'register/dashboard_supervisor.html')
        elif role == 'student':
            return render(request, 'register/dashboard_student.html')

    # If the user doesn't have a role or is not logged in, redirect to the login page
    return redirect('register:login')


def logout_view(request):
    logout(request)
    return redirect('register:login')
