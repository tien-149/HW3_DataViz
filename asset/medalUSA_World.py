import csv
import matplotlib.pyplot as plt 


categories = []
usa =[]
world = []

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1
		elif row[4] == "USA":
			usa.append([int(row[0]), row[5], row[6], row[7]]) #multidimensional array
		else:
			world.append([int(row[0]), row[5], row[6], row[7]]) 
		line_count += 1

print('Total medals of United States', len(usa))
print('Total medals of another country', len(world))

print('processed', line_count, 'rows of data')

total_medals = len(usa) + len(world)
usa_percentage = int(len(usa) / total_medals * 100)
world_percentage = int(len(world) / total_medals * 100)


labels = "United States", "World"
sizes = [usa_percentage, world_percentage]
colors = ('skyblue', 'yellow')
explode = (0.1, 0.1)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("Percentage of Medals in United States vs The world ")
plt.xlabel("Medals from 1024 to 2014")
plt.show()












