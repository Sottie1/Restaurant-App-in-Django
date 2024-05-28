from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from userauths.models import User
from .forms import SignUpForm
from django.contrib import messages

# Create your views here.

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             new_user = form.save()
#             username = form.cleaned_data.get('username')

#             messages.success(request, f"Hey,  {username} account created successfully")
#             new_user = authenticate(username = form.cleaned_data['email'], password = form.cleaned_data['password1'])
#             login(request, new_user)
#             return redirect('core:home')
        
#     else:
#         form = SignUpForm()
#     return render(request, 'userauths/signup.html', {'form': form})



# def login(request):
#     if request.user.is_authenticated:
#         return redirect('core:home')
    
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         try:
#             user = User.objects.get(email=email)
#             user = authenticate(email=email, password=password)

#             if user is not None:
#                 login(request, user)
#                 messages.success(request,f"You have successfully signed as {email}")
#                 return redirect('core:home')
#             else:
#                 messages.warning(request,f"User does not Exist: {email}")

#         except:
#             messages.warning(request,f"User with {email} does not Exist: ")

#     return render(request, "userauths/login.html",)
    

# def logout_view(request):
#     logout(request)
#     messages.success("User has been logged out")
#     return redirect('core:home')


# views.py

# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from .forms import SignUpForm
# from .models import User

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
    messages.success(request, "User has been logged out.")
    return redirect('core:home')
