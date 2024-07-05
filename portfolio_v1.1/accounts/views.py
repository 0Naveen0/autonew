from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import SignUpForm,LogInForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    
def LogInView(request):
    if request.method == "POST":        
        username = request.POST['username']
        if User.objects.filter(username=username).exists():
            password = request.POST['password']
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect("home")
            else:
                 messages.info(request, "Invalid Credentials.")
        else:
            messages.info(request, "User Not Exists.")           
    form_class = LogInForm
    return render(request,"registration/login.html",{'form':form_class})
    

    