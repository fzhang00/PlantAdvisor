from matplotlib import pyplot, dates
from csv import reader
from dateutil import parser

with open('microbit-data-13-2022-09-54-23-0400.csv', 'r') as f:
	data = list(reader(f, delimiter = "\t"))

light = [float(i[1]) for i in data[2:-1]]
time = [float(i[0]) for i in data[2:-1]]
hour = []
threshold = 200
accumulated = 0

for t in time:
    hour.append(t/60/60)
for i in  range(1, len(time)):
    if light[i]>threshold:
        accumulated = accumulated + (hour[i] - hour[i-1])
    else:
        pass
pyplot.title('The Light That Changes Over Time')
pyplot.xlabel('Time, (hours)')
pyplot.ylabel("The Light")
pyplot.xticks(rotation = 45)
pyplot.plot(hour, light)
print("time recorded","13-2022-09-54-23-0400".split("-"))
print("Hours of Sun Light the Plant has Gotten is", accumulated)
pyplot.show()



