from django.urls import path
from . import views


# Contains paths for lorchidee app
app_name = 'lorchidee'

urlpatterns = [
    path('index', views.index, name='index'),
    path('insertPlanning', views.insertPlanning, name='insertPlanning'),
    path('viewPlanning', views.viewPlanning, name='viewPlanning'),
    path('saveComment', views.saveComment, name='saveComment'),
]