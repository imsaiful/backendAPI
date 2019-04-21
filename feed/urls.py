from django.urls import path,include
from feed import views
from .views import CustomAuthToken

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('api-token-auth/', CustomAuthToken.as_view())

]
