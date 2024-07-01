from django.shortcuts import render
from pages.models import Colors

# Create your views here.
def home(request):
    return render(request,'pages/home.html',{})
    
def colors(request):
    colors = Colors.objects.all()
    context = {'title':'colors','colors':colors,}
    return render(request,'pages/colors.html',context)