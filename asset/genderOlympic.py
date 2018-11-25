import csv
import matplotlib.pyplot as plt 
import numpy as np

men = []
women = []

catagories = []

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			#print('tripping out catagories')
			catagories.append(row)
			line_count += 1
		else:
			if row[5] == "Men":
				#print('gold')
				men.append(row[5])
			elif row[5] == "Women":
				#print('silver')
				women.append(row[5])
			line_count += 1
print('Number of men', len(men))
print('Number of women', len(women))

m = len(men)
f = len(women)

print('processed', line_count, 'rows of data')

x = np.arange(2)
gender = [m,f]

fig, ax = plt.subplots()
plt.bar(x, gender, width=0.5, bottom=None, color='pink')

plt.xticks(x, ('Total men', 'Total women'))
plt.title("Number of man and woman in Olympic Winter since 1924 ", fontsize=14)
plt.show()














