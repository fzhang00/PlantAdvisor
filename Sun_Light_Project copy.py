from matplotlib import pyplot, dates
from csv import reader
from dateutil import parser

with open('microbit-data-27-2022-09-41-28-0500.csv', 'r') as f:
	data = list(reader(f, delimiter = "\t"))

light = [float(i[1]) for i in data[2:-1]]
time = [float(i[0]) for i in data[2:-1]]

pyplot.title('The Light That Changes Over Time 27-2022-09-41-28-0500')
pyplot.xlabel('Time/hours')
pyplot.ylabel("The Light")
pyplot.xticks(rotation = 45)
pyplot.plot(time, light)
pyplot.show()



