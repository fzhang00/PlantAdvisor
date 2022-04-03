from matplotlib import pyplot, dates
from csv import reader
from dateutil import parser

with open('microbit-data-13-2022-09-54-23-0400.csv', 'r') as f:
	data = list(reader(f, delimiter = "\t"))

light = [float(i[1]) for i in data[2:-1]]
time = [float(i[0]) for i in data[2:-1]]
threshold = 200
accumulated = 0

for i in  range(1, len(time)):
    if light[i]>threshold:
        accumulated = accumulated + (time[i] - time[i-1])
    else:
        pass
pyplot.title('The Light That Changes Over Time 27-2022-09-41-28-0500')
pyplot.xlabel('Time, (seconds')
pyplot.ylabel("The Light")
pyplot.xticks(rotation = 45)
pyplot.plot(time, light)
print("accumulated", accumulated)

pyplot.show()



