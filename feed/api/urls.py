from django.urls import path
from .views import AnchorListView, NewsChannelListView, CountlListView, \
    ReviewListView, TrendingListView, \
    NdtvListView, RepublicListView, IndianexpressListView, IndiatvListView, \
    ZeenewsListView, ThehinduListView, HindustanListView, FirstpostListView, News18ListView, OneindiaListView, \
    FindKeyWordNews,login



urlpatterns = [

    path('', NewsChannelListView.as_view()),
    path('review', ReviewListView.as_view()),
    path('login', login),
    path('trending', TrendingListView.as_view()),
    path('keyword/<slug:keyword>/', FindKeyWordNews.as_view(), name='keyword'),
    path('count/<int:pk>', CountlListView.as_view()),
    path('count', CountlListView.as_view()),
    path('ndtv', NdtvListView.as_view()),
    path('republic', RepublicListView.as_view()),
    path('indianexpress', IndianexpressListView.as_view()),
    path('indiatv', IndiatvListView.as_view()),
    path('thehindu', ThehinduListView.as_view()),
    path('hindustan', HindustanListView.as_view()),
    path('firstspot', FirstpostListView.as_view()),
    path('news18', News18ListView.as_view()),
    path('oneindia', OneindiaListView.as_view()),
    path('zeenews', ZeenewsListView.as_view()),
]
