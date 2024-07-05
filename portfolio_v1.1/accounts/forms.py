from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

# Create your forms here.
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = {'username','email','password1','password2'}
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Type User Name Here',
        'class':'form-control'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Type Email Here',
        'class':'form-control'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Type Password Here',
        'class':'form-control'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Repeat Password ',
        'class':'form-control'
    }))
    
class LogInForm(AuthenticationForm):    
    username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder':'Type User Name Here',
            'class':'form-control'
        }))  
    password = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder':'Type Password Here',
            'class':'form-control'
        }))        
        
      
    
