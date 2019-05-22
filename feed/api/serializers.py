from rest_framework import serializers
from feed.models import Anchor, News_Channel, Count, Review,IndexTop10,\
    Ndtv,Republic,Indianexpress,Indiatv,Zeenews,\
    Thehindu,Hindustan,Firstpost,News18,Oneindia


class AnchorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Anchor
        fields = ('name', 'channel_name', 'wiki', 'image')


class NewsChannelSerializers(serializers.ModelSerializer):
    class Meta:
        model = News_Channel
        fields = ('id','name', 'info', 'image', 'website', 'total_star', 'total_user')


class CountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Count
        fields = ('id','userId', 'channelId', 'rate')


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('channel', 'user', 'text', 'website', 'date')






class TrendingSerializers(serializers.ModelSerializer):
    class Meta:
        model = IndexTop10
        fields = ('db_keyword', 'db_frequency')





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

class TheHinduSerializers(serializers.ModelSerializer):
    class Meta:
        model = Thehindu
        fields = ('headline', 'link', 'date', 'category', 'sentiment')


class IndianexpressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Indianexpress
        fields = ('headline', 'link', 'date', 'category', 'sentiment')

class IndiatvSerializers(serializers.ModelSerializer):
    class Meta:
        model = Indiatv
        fields = ('headline', 'link', 'date', 'category', 'sentiment')


class ZeenewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Zeenews
        fields = ('headline', 'link', 'date', 'category', 'sentiment')


class HindustanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hindustan
        fields = ('headline', 'link', 'date', 'category', 'sentiment')




class News18Serializers(serializers.ModelSerializer):
    class Meta:
        model = News18
        fields = ('headline', 'link', 'date', 'category', 'sentiment')


class OneindiaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Oneindia
        fields = ('headline', 'link', 'date', 'category', 'sentiment')


class FirstpostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Firstpost
        fields = ('headline', 'link', 'date', 'category', 'sentiment')


