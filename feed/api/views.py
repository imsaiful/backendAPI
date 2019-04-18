from rest_framework.generics import ListAPIView, RetrieveAPIView
from feed.models import Anchor,News_Channel,Count,Review,IndexTop10
from .serializers import (AnchorSerializers,NewsChannelSerializers,
                          CountSerializers,ReviewSerializers,TrendingSerializers)


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
