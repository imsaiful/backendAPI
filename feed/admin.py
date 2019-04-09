from django.contrib import admin

from .models import (Anchor,News_Channel,Count,Review,
    Republic,Ndtv,News18,Indiatoday,Zeenews,
    Thehindu,Hindustan,IndexTop10,Dna,
    Indianexpress,Oneindia)

admin.site.register(Anchor)
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
admin.site.register(Indiatoday)
admin.site.register(Dna)
admin.site.register(IndexTop10)





# Register your models here.
