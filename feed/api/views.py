from itertools import chain
from drf_multiple_model.views import ObjectMultipleModelAPIView
from django.db.models import Q
from rest_framework.generics import ListAPIView, RetrieveAPIView,UpdateAPIView
from feed.models import Anchor, News_Channel, Count, Review, \
    IndexTop10, Ndtv, Republic, Indianexpress, Indiatv, Zeenews, Thehindu, Hindustan, Firstpost, News18, Oneindia
from .serializers import (AnchorSerializers, NewsChannelSerializers,
                          CountSerializers, ReviewSerializers, TrendingSerializers,
                          RepublicSerializers, NdtvSerializers, ZeeNewsSerializers,
                          OneindiaSerializers, News18Serializers, IndianexpressSerializers,
                          HindustanSerializers, FirstpostSerializers, IndiatvSerializers, TheHinduSerializers

                          )




class AnchorListView(ListAPIView):
    queryset = Anchor.objects.all()
    serializer_class = AnchorSerializers


class NewsChannelListView(ListAPIView):
    queryset = News_Channel.objects.all()
    serializer_class = NewsChannelSerializers


class CountlListView(ListAPIView):
    serializer_class = CountSerializers

    def get_queryset(self, *args, **kwargs):
        userId = self.kwargs.get('pk')
        queryset = Count.objects.filter(userId=userId)
        print(userId)
        return queryset


class ReviewListView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers


class TrendingListView(ListAPIView):
    queryset = IndexTop10.objects.all()
    serializer_class = TrendingSerializers


class NdtvListView(ListAPIView):
    queryset = Ndtv.objects.all()[0:10]
    serializer_class = NdtvSerializers



class IndianexpressListView(ListAPIView):
    queryset = Indianexpress.objects.all()[0:10]
    serializer_class = IndianexpressSerializers


class RepublicListView(ListAPIView):
    queryset = Republic.objects.all()[0:10]
    serializer_class = RepublicSerializers


class IndiatvListView(ListAPIView):
    queryset = Indiatv.objects.all()[0:10]
    serializer_class = IndiatvSerializers


class HindustanListView(ListAPIView):
    queryset = Hindustan.objects.all()[0:10]
    serializer_class = HindustanSerializers


class ZeenewsListView(ListAPIView):
    queryset = Zeenews.objects.all()[0:10]
    serializer_class = ZeeNewsSerializers


class FirstpostListView(ListAPIView):
    queryset = Firstpost.objects.all()[0:10]
    serializer_class = FirstpostSerializers


class News18ListView(ListAPIView):
    queryset = News18.objects.all()[0:10]
    serializer_class = News18Serializers


class OneindiaListView(ListAPIView):
    queryset = Oneindia.objects.all()[0:10]
    serializer_class = NdtvSerializers


class ThehinduListView(ListAPIView):
    queryset = Thehindu.objects.all()[0:10]
    serializer_class = TheHinduSerializers


class FindKeyWordNews(ObjectMultipleModelAPIView):
    querylist = []

    def get_querylist(self, *args, **kwargs):
        keyword = self.kwargs.get("keyword")
        print(keyword)
        if keyword:
            queryset = [
                {'queryset': Republic.objects.filter(Q(headline__icontains=keyword)).order_by('-id'),
                 'serializer_class': RepublicSerializers},
                {'queryset': Ndtv.objects.filter(Q(headline__icontains=keyword)).order_by('-id'),
                 'serializer_class': NdtvSerializers},
                {'queryset': Indiatv.objects.filter(Q(headline__icontains=keyword)).order_by('-id'),
                 'serializer_class': IndiatvSerializers},
                {'queryset': Hindustan.objects.filter(Q(headline__icontains=keyword)).order_by('-id'),
                 'serializer_class': HindustanSerializers},
                {'queryset': Thehindu.objects.filter(Q(headline__icontains=keyword)).order_by('-id'),
                 'serializer_class': TheHinduSerializers},
                {'queryset': Zeenews.objects.filter(Q(headline__icontains=keyword)).order_by('-id'),
                 'serializer_class': ZeeNewsSerializers},
                {'queryset': News18.objects.filter(Q(headline__icontains=keyword)).order_by('-id'),
                 'serializer_class': News18Serializers},
                {'queryset': Firstpost.objects.filter(Q(headline__icontains=keyword)).order_by('-id'),
                 'serializer_class': FirstpostSerializers},
                {'queryset': Indianexpress.objects.filter(Q(headline__icontains=keyword)).order_by('-id'),
                 'serializer_class': IndianexpressSerializers},
                {'queryset': Oneindia.objects.filter(Q(headline__icontains=keyword)).order_by('-id'),
                 'serializer_class': OneindiaSerializers},
            ]

            return queryset
