from feed.models import Ndtv, \
    Indiatv, \
    Republic, Indianexpress, Zeenews, \
    Thehindu, Hindustan, Firstpost, News18, Oneindia,CategoryRatio


def run():
    Republic_politics = Republic.objects.filter(category='politics').count()
    Republic_accident = Republic.objects.filter(category='accident').count()
    Republic_health = Republic.objects.filter(category='health').count()
    Republic_lifestyle = Republic.objects.filter(category='lifestyle').count()
    Republic_pollution = Republic.objects.filter(category='pollution').count()
    Republic_security = Republic.objects.filter(category='security').count()
    Republic_education = Republic.objects.filter(category='education').count()
    Republic_world = Republic.objects.filter(category='world').count()
    Republic_entertainment = Republic.objects.filter(category='entertainment').count()
    Republic_sports = Republic.objects.filter(category='sports').count()
    Republic_business = Republic.objects.filter(category='business').count()
    Republic_terrorism = Republic.objects.filter(category='terrorism').count()
    Republic_crime = Republic.objects.filter(category='crime').count()
    Republic_employment = Republic.objects.filter(category='employment').count()
    Republic_technology = Republic.objects.filter(category='technology').count()

    Ndtv_politics = Ndtv.objects.filter(category='politics').count()
    Ndtv_accident = Ndtv.objects.filter(category='accident').count()
    Ndtv_health = Ndtv.objects.filter(category='health').count()
    Ndtv_lifestyle = Ndtv.objects.filter(category='lifestyle').count()
    Ndtv_pollution = Ndtv.objects.filter(category='pollution').count()
    Ndtv_security = Ndtv.objects.filter(category='security').count()
    Ndtv_education = Ndtv.objects.filter(category='education').count()
    Ndtv_world = Ndtv.objects.filter(category='world').count()
    Ndtv_entertainment = Ndtv.objects.filter(category='entertainment').count()
    Ndtv_sports = Ndtv.objects.filter(category='sports').count()
    Ndtv_business = Ndtv.objects.filter(category='business').count()
    Ndtv_terrorism = Ndtv.objects.filter(category='terrorism').count()
    Ndtv_crime = Ndtv.objects.filter(category='crime').count()
    Ndtv_employment = Ndtv.objects.filter(category='employment').count()
    Ndtv_technology = Ndtv.objects.filter(category='technology').count()

    Indiatv_politics = Indiatv.objects.filter(category='politics').count()
    Indiatv_accident = Indiatv.objects.filter(category='accident').count()
    Indiatv_health = Indiatv.objects.filter(category='health').count()
    Indiatv_lifestyle = Indiatv.objects.filter(category='lifestyle').count()
    Indiatv_pollution = Indiatv.objects.filter(category='pollution').count()
    Indiatv_security = Indiatv.objects.filter(category='security').count()
    Indiatv_education = Indiatv.objects.filter(category='education').count()
    Indiatv_world = Indiatv.objects.filter(category='world').count()
    Indiatv_entertainment = Indiatv.objects.filter(category='entertainment').count()
    Indiatv_sports = Indiatv.objects.filter(category='sports').count()
    Indiatv_business = Indiatv.objects.filter(category='business').count()
    Indiatv_terrorism = Indiatv.objects.filter(category='terrorism').count()
    Indiatv_crime = Indiatv.objects.filter(category='crime').count()
    Indiatv_employment = Indiatv.objects.filter(category='employment').count()
    Indiatv_technology = Indiatv.objects.filter(category='technology').count()

    Hindustan_politics = Hindustan.objects.filter(category='politics').count()
    Hindustan_accident = Hindustan.objects.filter(category='accident').count()
    Hindustan_health = Hindustan.objects.filter(category='health').count()
    Hindustan_lifestyle = Hindustan.objects.filter(category='lifestyle').count()
    Hindustan_pollution = Hindustan.objects.filter(category='pollution').count()
    Hindustan_security = Hindustan.objects.filter(category='security').count()
    Hindustan_education = Hindustan.objects.filter(category='education').count()
    Hindustan_world = Hindustan.objects.filter(category='world').count()
    Hindustan_entertainment = Hindustan.objects.filter(category='entertainment').count()
    Hindustan_sports = Hindustan.objects.filter(category='sports').count()
    Hindustan_business = Hindustan.objects.filter(category='business').count()
    Hindustan_terrorism = Hindustan.objects.filter(category='terrorism').count()
    Hindustan_crime = Hindustan.objects.filter(category='crime').count()
    Hindustan_employment = Hindustan.objects.filter(category='employment').count()
    Hindustan_technology = Hindustan.objects.filter(category='technology').count()

    Thehindu_politics = Thehindu.objects.filter(category='politics').count()
    Thehindu_accident = Thehindu.objects.filter(category='accident').count()
    Thehindu_health = Thehindu.objects.filter(category='health').count()
    Thehindu_lifestyle = Thehindu.objects.filter(category='lifestyle').count()
    Thehindu_pollution = Thehindu.objects.filter(category='pollution').count()
    Thehindu_security = Thehindu.objects.filter(category='security').count()
    Thehindu_education = Thehindu.objects.filter(category='education').count()
    Thehindu_world = Thehindu.objects.filter(category='world').count()
    Thehindu_entertainment = Thehindu.objects.filter(category='entertainment').count()
    Thehindu_sports = Thehindu.objects.filter(category='sports').count()
    Thehindu_business = Thehindu.objects.filter(category='business').count()
    Thehindu_terrorism = Thehindu.objects.filter(category='terrorism').count()
    Thehindu_crime = Thehindu.objects.filter(category='crime').count()
    Thehindu_employment = Thehindu.objects.filter(category='employment').count()
    Thehindu_technology = Thehindu.objects.filter(category='technology').count()

    Zeenews_politics = Zeenews.objects.filter(category='politics').count()
    Zeenews_accident = Zeenews.objects.filter(category='accident').count()
    Zeenews_health = Zeenews.objects.filter(category='health').count()
    Zeenews_lifestyle = Zeenews.objects.filter(category='lifestyle').count()
    Zeenews_pollution = Zeenews.objects.filter(category='pollution').count()
    Zeenews_security = Zeenews.objects.filter(category='security').count()
    Zeenews_education = Zeenews.objects.filter(category='education').count()
    Zeenews_world = Zeenews.objects.filter(category='world').count()
    Zeenews_entertainment = Zeenews.objects.filter(category='entertainment').count()
    Zeenews_sports = Zeenews.objects.filter(category='sports').count()
    Zeenews_business = Zeenews.objects.filter(category='business').count()
    Zeenews_terrorism = Zeenews.objects.filter(category='terrorism').count()
    Zeenews_crime = Zeenews.objects.filter(category='crime').count()
    Zeenews_employment = Zeenews.objects.filter(category='employment').count()
    Zeenews_technology = Zeenews.objects.filter(category='technology').count()

    Indianexpress_politics = Indianexpress.objects.filter(category='politics').count()
    Indianexpress_accident = Indianexpress.objects.filter(category='accident').count()
    Indianexpress_health = Indianexpress.objects.filter(category='health').count()
    Indianexpress_lifestyle = Indianexpress.objects.filter(category='lifestyle').count()
    Indianexpress_pollution = Indianexpress.objects.filter(category='pollution').count()
    Indianexpress_security = Indianexpress.objects.filter(category='security').count()
    Indianexpress_education = Indianexpress.objects.filter(category='education').count()
    Indianexpress_world = Indianexpress.objects.filter(category='world').count()
    Indianexpress_entertainment = Indianexpress.objects.filter(category='entertainment').count()
    Indianexpress_sports = Indianexpress.objects.filter(category='sports').count()
    Indianexpress_business = Indianexpress.objects.filter(category='business').count()
    Indianexpress_terrorism = Indianexpress.objects.filter(category='terrorism').count()
    Indianexpress_crime = Indianexpress.objects.filter(category='crime').count()
    Indianexpress_employment = Indianexpress.objects.filter(category='employment').count()
    Indianexpress_technology = Indianexpress.objects.filter(category='technology').count()

    Firstpost_politics = Firstpost.objects.filter(category='politics').count()
    Firstpost_accident = Firstpost.objects.filter(category='accident').count()
    Firstpost_health = Firstpost.objects.filter(category='health').count()
    Firstpost_lifestyle = Firstpost.objects.filter(category='lifestyle').count()
    Firstpost_pollution = Firstpost.objects.filter(category='pollution').count()
    Firstpost_security = Firstpost.objects.filter(category='security').count()
    Firstpost_education = Firstpost.objects.filter(category='education').count()
    Firstpost_world = Firstpost.objects.filter(category='world').count()
    Firstpost_entertainment = Firstpost.objects.filter(category='entertainment').count()
    Firstpost_sports = Firstpost.objects.filter(category='sports').count()
    Firstpost_business = Firstpost.objects.filter(category='business').count()
    Firstpost_terrorism = Firstpost.objects.filter(category='terrorism').count()
    Firstpost_crime = Firstpost.objects.filter(category='crime').count()
    Firstpost_employment = Firstpost.objects.filter(category='employment').count()
    Firstpost_technology = Firstpost.objects.filter(category='technology').count()

    News18_politics = News18.objects.filter(category='politics').count()
    News18_accident = News18.objects.filter(category='accident').count()
    News18_health = News18.objects.filter(category='health').count()
    News18_lifestyle = News18.objects.filter(category='lifestyle').count()
    News18_pollution = News18.objects.filter(category='pollution').count()
    News18_security = News18.objects.filter(category='security').count()
    News18_education = News18.objects.filter(category='education').count()
    News18_world = News18.objects.filter(category='world').count()
    News18_entertainment = News18.objects.filter(category='entertainment').count()
    News18_sports = News18.objects.filter(category='sports').count()
    News18_business = News18.objects.filter(category='business').count()
    News18_terrorism = News18.objects.filter(category='terrorism').count()
    News18_crime = News18.objects.filter(category='crime').count()
    News18_employment = News18.objects.filter(category='employment').count()
    News18_technology = News18.objects.filter(category='technology').count()

    Oneindia_politics = Oneindia.objects.filter(category='politics').count()
    Oneindia_accident = Oneindia.objects.filter(category='accident').count()
    Oneindia_health = Oneindia.objects.filter(category='health').count()
    Oneindia_lifestyle = Oneindia.objects.filter(category='lifestyle').count()
    Oneindia_pollution = Oneindia.objects.filter(category='pollution').count()
    Oneindia_security = Oneindia.objects.filter(category='security').count()
    Oneindia_education = Oneindia.objects.filter(category='education').count()
    Oneindia_world = Oneindia.objects.filter(category='world').count()
    Oneindia_entertainment = Oneindia.objects.filter(category='entertainment').count()
    Oneindia_sports = Oneindia.objects.filter(category='sports').count()
    Oneindia_business = Oneindia.objects.filter(category='business').count()
    Oneindia_terrorism = Oneindia.objects.filter(category='terrorism').count()
    Oneindia_crime = Oneindia.objects.filter(category='crime').count()
    Oneindia_employment = Oneindia.objects.filter(category='employment').count()
    Oneindia_technology = Oneindia.objects.filter(category='technology').count()

    politics = Republic_politics + Ndtv_politics + Zeenews_politics + \
               News18_politics + Hindustan_politics + Indianexpress_politics + \
               Oneindia_politics + Firstpost_politics + Thehindu_politics + Indiatv_politics

    accident = Republic_accident + Ndtv_accident + Zeenews_accident + \
               News18_accident + Hindustan_accident + Indianexpress_accident + \
               Oneindia_accident + Firstpost_accident + Thehindu_accident + Indiatv_accident

    health = Republic_health + Ndtv_health + Zeenews_health + \
             News18_health + Hindustan_health + Indianexpress_health + \
             Oneindia_health + Firstpost_health + Thehindu_health + Indiatv_health

    lifestyle = Republic_lifestyle + Ndtv_lifestyle + Zeenews_lifestyle + \
                News18_lifestyle + Hindustan_lifestyle + Indianexpress_lifestyle + \
                Oneindia_lifestyle + Firstpost_lifestyle + Thehindu_lifestyle + Indiatv_lifestyle

    pollution = Republic_pollution + Ndtv_pollution + Zeenews_pollution + \
                News18_pollution + Hindustan_pollution + Indianexpress_pollution + \
                Oneindia_pollution + Firstpost_pollution + Thehindu_pollution + Indiatv_pollution

    security = Republic_security + Ndtv_security + Zeenews_security + \
               News18_security + Hindustan_security + Indianexpress_security + \
               Oneindia_security + Firstpost_security + Thehindu_security + Indiatv_security

    education = Republic_education + Ndtv_education + Zeenews_education + \
                News18_education + Hindustan_education + Indianexpress_education + \
                Oneindia_education + Firstpost_education + Thehindu_education + Indiatv_education

    world = Republic_world + Ndtv_world + Zeenews_world + \
            News18_world + Hindustan_world + Indianexpress_world + \
            Oneindia_world + Firstpost_world + Thehindu_world + Indiatv_world

    entertainment = Republic_entertainment + Ndtv_entertainment + Zeenews_entertainment + \
                    News18_entertainment + Hindustan_entertainment + Indianexpress_entertainment + \
                    Oneindia_entertainment + Firstpost_entertainment + Thehindu_entertainment + Indiatv_entertainment

    sports = Republic_sports + Ndtv_sports + Zeenews_sports + \
             News18_sports + Hindustan_sports + Indianexpress_sports + \
             Oneindia_sports + Firstpost_sports + Thehindu_sports + Indiatv_sports

    business = Republic_business + Ndtv_business + Zeenews_business + \
               News18_business + Hindustan_business + Indianexpress_business + \
               Oneindia_business + Firstpost_business + Thehindu_business + Indiatv_business

    terrorism = Republic_terrorism + Ndtv_terrorism + Zeenews_terrorism + \
                News18_terrorism + Hindustan_terrorism + Indianexpress_terrorism + \
                Oneindia_terrorism + Firstpost_terrorism + Thehindu_terrorism + Indiatv_terrorism

    crime = Republic_crime + Ndtv_crime + Zeenews_crime + \
            News18_crime + Hindustan_crime + Indianexpress_crime + \
            Oneindia_crime + Firstpost_crime + Thehindu_crime + Indiatv_crime

    employment = Republic_employment + Ndtv_employment + Zeenews_employment + \
                 News18_employment + Hindustan_employment + Indianexpress_employment + \
                 Oneindia_employment + Firstpost_employment + Thehindu_employment + Indiatv_employment

    technology = Republic_technology + Ndtv_technology + Zeenews_technology + \
                 News18_technology + Hindustan_technology + Indianexpress_technology + \
                 Oneindia_technology + Firstpost_technology + Thehindu_technology + Indiatv_technology

    total = politics + pollution + employment + accident + health + technology + crime + terrorism + \
            business + sports + entertainment + world + education + lifestyle + security

    print("politics", round(politics / total * 100,2), "%")
    print("pollution", round(pollution / total * 100,2), "%")
    print("Employment",round( employment / total * 100,2), "%")
    print("accident", round(accident / total * 100,2), "%")
    print("health", round(health / total * 100,2), "%")
    print("technology", round(technology / total * 100,2), "%")
    print("crime", round(crime / total * 100,2), "%")
    print("terrorism", round(terrorism / total * 100,2), "%")
    print("business", round(business / total * 100,2), "%")
    print("sports", round(sports / total * 100,2), "%")
    print("entertainment", round(entertainment / total * 100,2), "%")
    print("world", round(world / total * 100,2), "%")
    print("education", round(education / total * 100,2), "%")
    print("lifestyle", round(lifestyle / total * 100,2), "%")
    print("security", round(security / total * 100,2), "%")

    pk=0

    update=CategoryRatio(pk,"accident",round(accident / total * 100,2)).save()
    pk+=1
    update=CategoryRatio(pk,"health",round(health / total * 100,2)).save()
    pk += 1
    update=CategoryRatio(pk,"world",round(world / total * 100,2)).save()
    pk += 1
    update=CategoryRatio(pk,"lifestyle",round(lifestyle / total * 100,2)).save()
    pk += 1
    update=CategoryRatio(pk,"pollution",round(pollution / total * 100,2)).save()
    pk += 1
    update=CategoryRatio(pk,"pollution",round(security / total * 100,2)).save()
    pk += 1
    update=CategoryRatio(pk,"education",round(education / total * 100,2)).save()
    pk += 1
    update=CategoryRatio(pk,"entertainment",round(entertainment / total * 100,2)).save()
    pk += 1
    update=CategoryRatio(pk,"sports",round(sports / total * 100,2)).save()
    pk += 1
    update=CategoryRatio(pk,"politics",round(politics / total * 100,2)).save()
    pk += 1
    update=CategoryRatio(pk,"business",round(business / total * 100,2)).save()
    pk += 1
    update=CategoryRatio(pk,"terrorism",round(terrorism / total * 100,2)).save()
    pk += 1
    update=CategoryRatio(pk,"crime",round(crime / total * 100,2)).save()
    pk += 1
    update=CategoryRatio(pk,"employment",round( employment / total * 100,2)).save()
    pk += 1
    update=CategoryRatio(pk,"technology",round(technology / total * 100,2)).save()
    pk+=1
