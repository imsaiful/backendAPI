from django.urls import path
from .views import AnchorListView, NewsChannelListView


urlpatterns = [
    path('', NewsChannelListView.as_view()),
]
