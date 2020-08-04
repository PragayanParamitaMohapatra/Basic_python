import requests
import html5lib
import pandas as pd
from bs4 import BeautifulSoup
url="http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168"
response=requests.get(url)
soup=BeautifulSoup(response.content,'html.parser')
# print(soup.prettify())
seven_day = soup.find(id="seven-day-forecast")
print(seven_day)
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
print(tonight.prettify())
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
print(period)
print(short_desc)
print(temp)
img = tonight.find("img")
# beautifulsoup object as a dictionary and title is a key
desc = img['title']
print(desc)
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
print(periods)
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
print(short_descs)

print(temps)
print(descs)
weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc":descs
})
print(weather)
temp_num=weather["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
weather["temp_num"] = temp_num.astype('int')
print(temp_num)

is_night = weather["temp"].str.contains("Low")
weather["is_night"] = is_night
print(is_night)