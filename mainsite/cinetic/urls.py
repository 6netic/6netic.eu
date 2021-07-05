from django.urls import path
from . import views

# Contains paths for 6netic app
app_name = 'cinetic'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    #path('services', views.services, name='services'),
    path('projets', views.projets, name='projets'),
    path('contact', views.contact, name='contact'),
]
