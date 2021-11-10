import pandas as pd

weather = pd.read_csv("weather_data.txt")
precip = (weather.actual_precipitation == weather.actual_precipitation.max())
print("Day had the highest actual precipitation")
print(weather.loc[precip, "date"], "\n")

july = weather.loc[0:30, ["date", "actual_max_temp"]]
print("Average actual max temp for July 2014")
print(july.actual_max_temp.mean(), "\n")

temp = (weather.actual_max_temp == weather.record_max_temp)
print("Days the actual max temp was the record max temp")
print(weather.loc[temp, "date"], "\n")

oct = weather.loc[92:122, ["date", "actual_precipitation"]]
print("Rain in October 2014")
print(oct.actual_precipitation.sum(), "\n")

condition = (weather.actual_min_temp <= 60) & (weather.actual_max_temp >= 90)
print("Actual low temperature below 60 degrees and actual max temperature above 90 degrees on the same day")
print(weather.loc[condition, "date"])