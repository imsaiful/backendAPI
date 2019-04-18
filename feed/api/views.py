from rest_framework.generics import ListAPIView, RetrieveAPIView
from feed.models import Anchor,News_Channel,Count,Review,\
                        IndexTop10,Ndtv,Republic,Indianexpress,Indiatv,Zeenews,Thehindu,Hindustan,Firstpost,News18,Oneindia
from .serializers import (AnchorSerializers,NewsChannelSerializers,
                          CountSerializers,ReviewSerializers,TrendingSerializers,
                          NdtvSerializers)


class AnchorListView(ListAPIView):
    queryset = Anchor.objects.all()
    serializer_class = AnchorSerializers


class NewsChannelListView(ListAPIView):
    queryset = News_Channel.objects.all()
    serializer_class = NewsChannelSerializers



class CountlListView(ListAPIView):
    queryset = Count.objects.all()
    serializer_class = CountSerializers



class ReviewListView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

class TrendingListView(ListAPIView):
    queryset = IndexTop10.objects.all()
    serializer_class = TrendingSerializers

class NdtvListView(ListAPIView):
    queryset = Ndtv.objects.all()[0:5]
    serializer_class = NdtvSerializers

class IndianexpressListView(ListAPIView):
    queryset = Indianexpress.objects.all()[0:5]
    serializer_class = NdtvSerializers

class RepublicListView(ListAPIView):
    queryset = Republic.objects.all()[0:5]
    serializer_class = NdtvSerializers

class IndiatvListView(ListAPIView):
    queryset = Indiatv.objects.all()[0:5]
    serializer_class = NdtvSerializers


class HindustanListView(ListAPIView):
    queryset = Hindustan.objects.all()[0:5]
    serializer_class = NdtvSerializers


class ZeenewsListView(ListAPIView):
    queryset = Zeenews.objects.all()[0:5]
    serializer_class = NdtvSerializers


class FirstpostListView(ListAPIView):
    queryset = Firstpost.objects.all()[0:5]
    serializer_class = NdtvSerializers



class News18ListView(ListAPIView):
    queryset = News18.objects.all()[0:5]
    serializer_class = NdtvSerializers


class OneindiaListView(ListAPIView):
    queryset = Oneindia.objects.all()[0:5]
    serializer_class = NdtvSerializers

class ThehinduListView(ListAPIView):
    queryset = Thehindu.objects.all()[0:5]
    serializer_class = NdtvSerializers