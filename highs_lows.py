import csv

from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	for index, column_header in enumerate(header_row):
		print(index, column_header)
		
	dates, highs, lows = [], [], []
	for row in reader:
		current_date = datetime.strptime(row[0], "%Y-%m-%d")    # datetime.strptime has two parameters, the one is 													 			   														   
		dates.append(current_date)                              # the time object to be treated, the other help
		high = int(row[1])                                      # understand what these numbers stand for
		highs.append(high)
		
		low = int(row[3])
		lows.append(low)
	print(highs)

#draw the graph according to data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')

#set form of the graph
plt.title("Daily high and low temperatures, 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()



