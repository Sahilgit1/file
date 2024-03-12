from django.urls import path
from . import views
urlpatterns = [
    
path('', views.home, name='home'),
path('learn', views.learn, name='learn'),
path('login', views.login, name='login'),
path('practice', views.practice, name='login'),
path('jobs', views.jobs, name='login'),
path('homee', views.homee, name='home'),


]
