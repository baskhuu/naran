from django.urls import path
#inportin views from current directory(.)
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/', views.room, name="room"),
]
