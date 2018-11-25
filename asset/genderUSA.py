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
men_usa = []
women_usa = []

for medal in usa:
		if medal[1] == "Men":
			men_usa.append(medal)

		if medal[1] == "Women":
			women_usa.append(medal)

print('Number of men in USA' , len(men_usa))
print('Number of women in USA', len(women_usa))
print('processed', line_count, 'rows of data')

total_gender = len(women_usa) + len(men_usa)
men_percentage = int(len(men_usa) / total_gender * 100)
women_percentage = int(len(women_usa) / total_gender * 100)

labels = "Men", "Women"
sizes = [men_percentage, women_percentage]
colors = ('skyblue', 'pink')
explode = (0.1, 0.1)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("Percentage of men and women in USA ")
plt.xlabel("Olympic winter since 1924")
plt.show()





