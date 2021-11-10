import pandas as pd
import matplotlib.pyplot as plt

weather = pd.read_csv("weather_data.txt")

min = weather.actual_min_temp
max = weather.actual_max_temp
date = weather.date
plt.figure("Actual max temperature and actual min temperature")
plt.plot(date, min, color='blue', label="Min temp")
plt.plot(date, max, color='red', label="Max temp")
plt.plot()

plt.figure("Actual Precipitation")
weather["actual_precipitation"].plot(kind='hist', x='Actual Precipitation')
plt.show()