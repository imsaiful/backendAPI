from django.urls import path
from .views import AnchorListView, AnchorDetailView

urlpatterns = [
    path('', AnchorListView.as_view()),
    path('<pk>', AnchorDetailView.as_view()),
]
