import csv
import matplotlib.pyplot as plt 

categories = []
usa =[]

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1
		elif row[4] == "USA":
			usa.append([int(row[0]), row[5], row[6], row[7]])
		line_count += 1
			#Year   Gender   Sport  Medals
gold_usa = []
silver_usa = []
bronze_usa = []

for medal in usa:
	if medal[3] == "Gold":
	 gold_usa.append(medal)

	if medal[3] == "Silver":
	 silver_usa.append(medal)

	if medal[3] == "Bronze":
	 bronze_usa.append(medal)

print('Number of Gold medals in USA', len(gold_usa),'medals')
print('Number of Silver medals in USA', len(silver_usa), 'medals')
print('Number of Bronze medals in USA', len(bronze_usa), 'medals')
print('processed', line_count, 'rows of data')


total_medal = len(gold_usa) + len(silver_usa) + len(bronze_usa)
gold_percentage = int(len(gold_usa) / total_medal * 100)
silver_percentage = int(len(silver_usa) / total_medal * 100)
bronze_percentage = int(len(bronze_usa) / total_medal * 100)

labels = "Gold", "Silver", "Bronze"
sizes = [gold_percentage, silver_percentage, bronze_percentage]
colors = ('yellow', 'skyblue', 'orange')
explode = (0.1, 0.1, 0.15)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("Percentage of different kinds of medals in USA")
plt.xlabel("Medals in Olympic Winter since 1024")
plt.show()














