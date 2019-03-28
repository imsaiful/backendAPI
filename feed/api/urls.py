from django.urls import path
from .views import AnchorListView, NewsChannelListView,CountlListView,ReviewListView


urlpatterns = [
    path('', NewsChannelListView.as_view()),
    path('count', CountlListView.as_view()),
    path('review', ReviewListView.as_view()),
]
