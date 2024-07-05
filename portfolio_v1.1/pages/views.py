from django.shortcuts import render,redirect
from pages.models import Colors
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    return render(request,'pages/home.html',{})

@login_required(login_url='/accounts/login/')    
def colors(request):
    colors = Colors.objects.all()
    context = {'title':'colors','colors':colors,}
    return render(request,'pages/colors.html',context)