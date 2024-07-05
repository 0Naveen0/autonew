from django.urls import path
from .views import SignUpView,LogInView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name='signup'),
    path("login/", LogInView, name='login'),
    
]