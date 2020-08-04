#combing the data into pandas data frame because it stores data in a tabular form it helps to data analysis
import pandas as pd
from . import extract_weather_data

weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc":descs
})