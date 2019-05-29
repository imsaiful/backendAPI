from itertools import chain
from drf_multiple_model.views import ObjectMultipleModelAPIView
from django.db.models import Q
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from feed.models import News_Channel, Count, Review, \
    IndexTop10, Ndtv, Republic, Indianexpress, Indiatv, Zeenews, Thehindu, Hindustan, Firstpost, News18, Oneindia, \
    CategoryRatio, Jlist, JStarList
from .serializers import (NewsChannelSerializers,
                          CountSerializers, ReviewSerializers, TrendingSerializers,
                          RepublicSerializers, NdtvSerializers, ZeeNewsSerializers,
                          OneindiaSerializers, News18Serializers, IndianexpressSerializers,
                          HindustanSerializers, FirstpostSerializers, IndiatvSerializers,
                          TheHinduSerializers, CategoryRatioSerializer, JlistSerializers, JCountSerializers
                          )

from rest_framework_word_filter import FullWordSearchFilter
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    i = 1
    for i in range(1, 15):
        news_obj = News_Channel.objects.get(id=i)
        uid = User.objects.get(username=username)
        obj = Count.objects.filter(userId=uid, channelId=news_obj).count()
        print(i, " ", obj)
        if obj == 0:
            print("id===", user.id)
            o = Count.objects.create(userId=uid, channelId=news_obj,
                                     rate=0)
            o.save()
        i += 1
    n = Jlist.objects.all().count()

    for i in range(1, n + 1):
        j_obj = Jlist.objects.get(id=i)
        uid = User.objects.get(username=username)
        obj = JStarList.objects.filter(userId=uid, anchorId=j_obj).count()
        if obj == 0:
            print("id===", user.id)
            o = JStarList.objects.create(userId=uid, anchorId=j_obj,
                                         rate=0)
            o.save()
        i += 1

    token, _ = Token.objects.get_or_create(user=user)
    voting_result = Count.objects.filter(userId=user.id)
    print(voting_result)
    channel = {}

    for e in voting_result:
        channel[str(e.channelId)] = e.rate
    return Response({'token': token.key, 'user': user.username, 'email': user.email, 'id': user.id, 'stats': channel},
                    status=HTTP_200_OK)


class JlistView(ObjectMultipleModelAPIView):

    def get_querylist(self, *args, **kwargs):
        userId = self.kwargs.get('pk')
        queryset = [
            {'queryset': Jlist.objects.all(),
             'serializer_class': JlistSerializers},
            {'queryset': JStarList.objects.filter(userId=userId),
             'serializer_class': JCountSerializers }
        ]
        return queryset


class NewsChannelListView(ListAPIView):
    queryset = News_Channel.objects.all()

    def get_queryset(self, *args, **kwargs):
        userId = self.kwargs.get('pk')
        queryset = [
            {'queryset': News_Channel.objects.all(),
             'serializer_class': NewsChannelSerializers},
            {'queryset': Count.objects.filter(userId=userId),
             'serializer_class': NdtvSerializers},
        ]
        return queryset


class CountlListView(ListAPIView):
    serializer_class = CountSerializers

    def get_queryset(self, *args, **kwargs):
        userId = self.kwargs.get('pk')
        queryset = Count.objects.filter(userId=userId)
        print(userId)
        return queryset


class CountlUpdateView(UpdateAPIView):
    serializer_class = CountSerializers
    print("in")

    def get_queryset(self, *args, **kwargs):
        id = self.kwargs.get('pk')
        print(id)
        print(self.request.user)
        queryset = Count.objects.filter(pk=id)

        return queryset


class JCountlListView(ListAPIView):
    serializer_class = JCountSerializers

    def get_queryset(self, *args, **kwargs):
        userId = self.kwargs.get('pk')
        queryset = JStarList.objects.filter(userId=userId)
        print(userId)
        return queryset


class JCountlUpdateView(UpdateAPIView):
    serializer_class = JCountSerializers
    print("in")

    def get_queryset(self, *args, **kwargs):
        id = self.kwargs.get('pk')
        print(id)
        print(self.request.user)
        queryset = JStarList.objects.filter(pk=id)

        return queryset

    # 'CountlUpdateView' should either include a `serializer_class` attribute, or override the `get_serializer_class()` method.

    # def get_queryset(self, *args, **kwargs):
    #     userId = self.kwargs.get('pk')
    #     queryset = Count.objects.filter(userId=userId)
    #     print(userId)
    #     return queryset
    #
    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     if instance.userId==self.request.user.id:
    #         instance.rate = request.data.get("rate")
    #         instance.save()
    #
    #
    #     serializer = self.get_serializer(instance)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #
    #     return Response(serializer.data)


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


class NewsChannelListView(ObjectMultipleModelAPIView):

    def get_querylist(self, *args, **kwargs):
        userId = self.request.user.id
        queryset = [
            {'queryset': News_Channel.objects.all(),
             'serializer_class': NewsChannelSerializers},
            {'queryset': Count.objects.filter(userId=userId),
             'serializer_class': CountSerializers},
        ]
        return queryset


class FindKeyWordNews(ObjectMultipleModelAPIView):
    querylist = []
    filter_backends = (FullWordSearchFilter,)
    word_fields = ('text',)

    def get_querylist(self, *args, **kwargs):
        keyword = self.kwargs.get("keyword")
        print(keyword)
        if keyword:
            queryset = [
                {'queryset': Republic.objects.filter(Q(headline__icontains=keyword)).order_by('-id')[0:1],
                 'serializer_class': RepublicSerializers},
                {'queryset': Ndtv.objects.filter(Q(headline__icontains=keyword)).order_by('-id')[0:1],
                 'serializer_class': NdtvSerializers},
                {'queryset': Indiatv.objects.filter(Q(headline__icontains=keyword)).order_by('-id')[0:1],
                 'serializer_class': IndiatvSerializers},
                {'queryset': Hindustan.objects.filter(Q(headline__icontains=keyword)).order_by('-id')[0:1],
                 'serializer_class': HindustanSerializers},
                {'queryset': Thehindu.objects.filter(Q(headline__icontains=keyword)).order_by('-id')[0:1],
                 'serializer_class': TheHinduSerializers},
                {'queryset': Zeenews.objects.filter(Q(headline__icontains=keyword)).order_by('-id')[0:1],
                 'serializer_class': ZeeNewsSerializers},
                {'queryset': News18.objects.filter(Q(headline__icontains=keyword)).order_by('-id')[0:1],
                 'serializer_class': News18Serializers},
                {'queryset': Firstpost.objects.filter(Q(headline__icontains=keyword)).order_by('-id')[0:1],
                 'serializer_class': FirstpostSerializers},
                {'queryset': Indianexpress.objects.filter(Q(headline__icontains=keyword)).order_by('-id')[0:1],
                 'serializer_class': IndianexpressSerializers},
                {'queryset': Oneindia.objects.filter(Q(headline__icontains=keyword)).order_by('-id')[0:1],
                 'serializer_class': OneindiaSerializers},
            ]

            return queryset


class FindCategoryNews(ObjectMultipleModelAPIView):
    querylist = []

    def get_querylist(self, *args, **kwargs):
        keyword = self.kwargs.get("keyword")
        print(keyword)
        if keyword:
            queryset = [
                {'queryset': Republic.objects.filter(category=keyword).order_by('-id')[0:10],
                 'serializer_class': RepublicSerializers},
                {'queryset': Ndtv.objects.filter(category=keyword).order_by('-id')[0:10],
                 'serializer_class': NdtvSerializers},
                {'queryset': Indiatv.objects.filter(category=keyword).order_by('-id')[0:10],
                 'serializer_class': IndiatvSerializers},
                {'queryset': Hindustan.objects.filter(category=keyword).order_by('-id')[0:10],
                 'serializer_class': HindustanSerializers},
                {'queryset': Thehindu.objects.filter(category=keyword).order_by('-id')[0:10],
                 'serializer_class': TheHinduSerializers},
                {'queryset': Zeenews.objects.filter(category=keyword).order_by('-id')[0:10],
                 'serializer_class': ZeeNewsSerializers},
                {'queryset': News18.objects.filter(category=keyword).order_by('-id')[0:10],
                 'serializer_class': News18Serializers},
                {'queryset': Firstpost.objects.filter(category=keyword).order_by('-id')[0:10],
                 'serializer_class': FirstpostSerializers},
                {'queryset': Indianexpress.objects.filter(category=keyword).order_by('-id')[0:10],
                 'serializer_class': IndianexpressSerializers},
                {'queryset': Oneindia.objects.filter(category=keyword).order_by('-id')[0:10],
                 'serializer_class': OneindiaSerializers},
            ]

            return queryset


class CategorySerializers(ListAPIView):
    queryset = CategoryRatio.objects.all()
    serializer_class = CategoryRatioSerializer
