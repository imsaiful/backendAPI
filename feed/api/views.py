from rest_framework.generics import ListAPIView, RetrieveAPIView
from feed.models import Anchor,News_Channel,Count,Review
from .serializers import AnchorSerializers,NewsChannelSerializers,CountSerializers,ReviewSerializers


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
