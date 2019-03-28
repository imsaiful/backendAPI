from rest_framework.generics import ListAPIView, RetrieveAPIView
from feed.models import Anchor,News_Channel
from .serializers import AnchorSerializers,NewsChannelSerializers


class AnchorListView(ListAPIView):
    queryset = Anchor.objects.all()
    serializer_class = AnchorSerializers


class NewsChannelListView(ListAPIView):
    queryset = News_Channel.objects.all()
    serializer_class = NewsChannelSerializers
