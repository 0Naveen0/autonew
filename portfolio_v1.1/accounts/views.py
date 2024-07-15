from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import SignUpForm,LogInForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import authenticate,login
from django.contrib import messages
from accounts.models import CustomUser

# Create your views here.
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    
def LogInView(request):
    if request.method == "POST":        
        username = request.POST['username']
        if User.objects.filter(username=username).exists():
            user = User.objects.filter(username=username).values().first()
            #print(user['id'])
            customuser=""
            #print(CustomUser.objects.get(user=user['id']))
            if  CustomUser.objects.filter(user=user['id']).count():
                customuser = CustomUser.objects.get(user=user['id'])
                print(customuser.company.id)
                print(customuser.company.company_name)
                print(customuser.user.id)
                print(customuser.user.username)
                print(customuser.user.email)           
            password = request.POST['password']
            users = authenticate(request,username=username, password=password)
            if users is not None:
                login(request,users)
                #login(request,customuser)
                if customuser:
                    request.session['companyid'] = customuser.company.id
                else:
                    request.session['companyid'] = False
                return redirect("home")
            else:
                 messages.info(request, "Invalid Credentials.")
        else:
            messages.info(request, "User Not Exists.")           
    form_class = LogInForm
    return render(request,"registration/login.html",{'form':form_class})
    

    