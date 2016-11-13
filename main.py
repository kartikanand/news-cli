import requests
import feedparser

google_news_url = 'https://news.google.co.in/news?cf=all&hl=en&pz=1&ned=in&output=rss'

r = requests.get(google_news_url)

if r.status_code != 200:
    print('not able to reach server')
    exit()

data = feedparser.parse(r.text)

title = data.feed.title
description = data.feed.description
published_date = data.feed.published

print(title)
print(description)
print(published_date)

for entry in data.entries:
    print(entry.title)

