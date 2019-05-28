from django.contrib import admin

from .models import (News_Channel,Count,Review,
    Republic,Ndtv,News18,Indiatv,Zeenews,
    Thehindu,Hindustan,IndexTop10,Dna,
    Indianexpress,Oneindia,CategoryRatio,Jlist,JStarList)

admin.site.register(Jlist)
admin.site.register(JStarList)
admin.site.register(News_Channel)
admin.site.register(Count)
admin.site.register(Review)
admin.site.register(Republic)
admin.site.register(Ndtv)
admin.site.register(Zeenews)
admin.site.register(Thehindu)
admin.site.register(News18)
admin.site.register(Hindustan)
admin.site.register(Indianexpress)
admin.site.register(Oneindia)
admin.site.register(Indiatv)
admin.site.register(Dna)
admin.site.register(IndexTop10)
admin.site.register(CategoryRatio)





# Register your models here.
