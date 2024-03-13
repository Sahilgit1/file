from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
path('', views.home, name='home'),
path('learn', views.learn, name='learn'),
path('login', views.login, name='login'),
path('practice', views.practice, name='login'),
path('jobs', views.jobs, name='login'),
path('homee', views.homee, name='home'),


]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
