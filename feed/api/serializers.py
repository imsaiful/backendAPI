from rest_framework import serializers
from feed.models import Anchor, News_Channel


class AnchorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Anchor
        fields = ('name', 'channel_name', 'wiki', 'image')


class NewsChannelSerializers(serializers.ModelSerializer):
    class Meta:
        model = News_Channel
        fields = ('name', 'info', 'image', 'website', 'total_star', 'total_user')
