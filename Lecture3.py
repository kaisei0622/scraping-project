# 天気予報API取得
import requests

r = requests.get("https://weather.tsukumijima.net/api/forecast/city/170020")

# print(r.json())
#
# #forecastsのキーを取得する
# print(r.json()["forecasts"])
#
# #リストの長さを確認する
# print(len(r.json()["forecasts"]))

for i in range(0,3):
    print(r.json()["forecasts"][i]["date"])
    print(r.json()["forecasts"][i]["telop"])
    print(r.json()["forecasts"][i]["temperature"]["max"]["celsius"])