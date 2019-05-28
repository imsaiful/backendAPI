from feed.models import Ndtv, \
    IndexTop10, \
    Republic, Indianexpress, Indiatv, Zeenews, \
    Thehindu, Hindustan, Firstpost, News18, Oneindia, Count, News_Channel
from feed.models import User


def run():
    for i in range(1, 15):
        news_channel = Count.objects.filter(channelId=i)
        total_rate = 0
        total_user = 1
        for rate in news_channel:
            total_rate += rate.rate
            if rate.rate > 0:
                total_user += 1
        print(total_user)
        object = News_Channel.objects.filter(id=i)
        object.update(total_star=total_rate)
        object.update(total_user=total_user)
