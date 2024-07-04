from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse
from accounts.forms import register
# Create your views here.

def login_view(request):
    if not  request.user.is_authenticated:
        if request.method == "POST":
            # form = AuthenticationForm(request=request, data=request.POST)
            # if form.is_valid():
                username = request.POST["username"]
                password = request.POST["password"]
                user = authenticate(request, username=username, password=password)
                if user is not None:
                        login(request, user)
                        messages.add_message(request, messages.SUCCESS,f"login user as {request.user.username}")
                        return redirect('/')
                else:
                      messages.add_message(request, messages.ERROR,"Failed username/email or password ")   
        # form = AuthenticationForm()        
        return render(request,'accounts/login.html')
    else:
        messages.add_message(request, messages.ERROR,f"user is authenticated as {request.user.username}")
        return redirect('/')

@login_required
def logout_view(request):
        logout(request)
        messages.add_message(request, messages.SUCCESS,"logout successfully")
        return redirect('/')

        
def register_view(request):
    if not  request.user.is_authenticated:
        if request.method == "POST":
            form = register(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS,"User Creating successfully")
                return redirect('/') 

            else:
                messages.add_message(request, messages.ERROR,"Failed User Created")       
        form = register()
        context ={"form":form}
        return render(request, 'accounts/register.html', context)
    else:
        messages.add_message(request, messages.ERROR,"Your are login in  ") 
        return redirect('/')      