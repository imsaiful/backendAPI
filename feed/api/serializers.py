from rest_framework import serializers
from feed.models import Anchor


class AnchorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Anchor
        fields = ('name', 'channel_name', 'wiki,image')
