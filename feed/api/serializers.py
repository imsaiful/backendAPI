from rest_framework import serializers
from feed.models import Anchor, News_Channel , Count , Review ,Republic,Ndtv,Hindustan,Thehindu,IndexTop10


class AnchorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Anchor
        fields = ('name', 'channel_name', 'wiki', 'image')


class NewsChannelSerializers(serializers.ModelSerializer):
    class Meta:
        model = News_Channel
        fields = ('name', 'info', 'image', 'website', 'total_star', 'total_user')


class CountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Count
        fields = ('userId', 'channelId', 'rate')


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('channel', 'user', 'text', 'website', 'date')

class RepublicSerializers(serializers.ModelSerializer):
    class Meta:
        model = Republic
        fields = ('headline', 'link', 'date', 'category', 'sentiment')

class NdtvSerializers(serializers.ModelSerializer):
    class Meta:
        model =Ndtv
        fields = ('headline', 'link', 'date', 'category', 'sentiment')

class ZeeNewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Thehindu
        fields = ('headline', 'link', 'date', 'category', 'sentiment')

class TrendingSerializers(serializers.ModelSerializer):
    class Meta:
        model = IndexTop10
        fields = ('db_keyword', 'db_frequency')



