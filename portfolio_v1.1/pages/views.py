from django.shortcuts import render,redirect
from pages.models import Colors
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser,Company

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    #customuser = CustomUser.objects.get(user=request.user.id)
    #company = Company.objects.get(pk=request.session.get('companyid'))
    #print(customuser.company.id)
    #print(customuser.company.company_name)
    #print(customuser.user.id)
    #print(customuser.user.username)
    #print(customuser.user.email)
    if request.session.get('companyid') :
        context={
            'company':Company.objects.get(pk=request.session.get('companyid'))
        }
    else :
        context={
            'company':False
        }
    
    return render(request,'pages/home.html',context)

@login_required(login_url='/accounts/login/')    
def colors(request):
    colors = Colors.objects.all()
    context = {'title':'colors','colors':colors,}
    return render(request,'pages/colors.html',context)