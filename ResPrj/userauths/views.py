from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from userauths.models import User
from .forms import SignUpForm
from django.contrib import messages



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Hey, {username}, your account was created successfully!")
            # Authenticate and login with the username instead of email
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            if new_user is not None:
                login(request, new_user)
                return redirect('core:home')
            else:
                messages.warning(request, "Authentication failed. Please try logging in manually.")
    else:
        form = SignUpForm()
    return render(request, 'userauths/signup.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('core:home')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user = authenticate(username=user.username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"You have successfully signed in as {email}")
                return redirect('core:home')
            else:
                messages.warning(request, "Invalid credentials, please try again.")
        except User.DoesNotExist:
            messages.warning(request, f"User with email {email} does not exist.")

    return render(request, 'userauths/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You has been logged out.")
    return redirect('core:home')
