from django.urls import path,include
from feed import views


urlpatterns = [
    path('', views.IndexView, name='index'),


]
