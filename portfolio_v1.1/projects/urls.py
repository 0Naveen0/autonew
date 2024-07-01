from django.urls import path
from projects import views

urlpatterns = [
    path("", views.projects_home, name='projects_home'),
    path("<int:pk>/", views.projects_detail, name='projects_detail'),
]