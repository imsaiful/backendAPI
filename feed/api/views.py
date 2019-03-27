from rest_framework.generics import ListAPIView,RetrieveAPIView
from feed.models import Anchor
from .serializers import AnchorSerializers

class AnchorListView(ListAPIView):
    queryset = Anchor.objects.all()
    serializer_class = AnchorSerializers


class AnchorDetailView(RetrieveAPIView):
    pass