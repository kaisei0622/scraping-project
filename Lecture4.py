# YahooニュースAPI取得

import pprint
import feedparser

data = feedparser.parse("https://news.yahoo.co.jp/rss/topics/domestic.xml")

# pprint.pprint(data)

# pprint.pprint(data["entries"])

# print(len(data["entries"]))

s = (len(data["entries"]))

for i in range(0, s):
    print(data["entries"][i]["title"])
    print(data["entries"][i]["published"])
    print(data["entries"][i]["link"])