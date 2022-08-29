from newsapi import NewsApiClient
from datetime import datetime, timedelta



lastHourDateTime = datetime.now() - timedelta(hours = 1)

current_time=lastHourDateTime.strftime("%H:%M:%S")
api = NewsApiClient(api_key='6ab79751a18d4bdd8fc11e6d03177554')

top_headlines=api.get_top_headlines(country='in')
sports=api.get_top_headlines(category='sports',country='in')
all_articles = api.get_everything(q='india')
technology=api.get_top_headlines(category="technology")


articles=top_headlines['articles']
sports=sports['articles']
all_articles=all_articles['articles']
technology=technology['articles']
context={
    "time":current_time,
    "top_headlines":articles,
    "sports":sports,
    "all_articles":all_articles,
    "technology":technology,

    }