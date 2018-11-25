import csv
import matplotlib.pyplot as plt 
import numpy as np

world_1924 = []
world_1928 = []
world_1932 = []
world_1936 = []
world_1948 = []
world_1952 = []
world_1956 = []
world_1960 = []
world_1964 = []
world_1968 = []
world_1972 = []
world_1976 = []
world_1980 = []
world_1984 = []
world_1988 = []
world_1992 = []
world_1994 = []
world_1998 = []
world_2002 = []
world_2006 = []
world_2010 = []
world_2014 = []

catagories = []

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			catagories.append(row)
			line_count += 1
		else:
			if row[0] == "1924":
				world_1924.append(row[0])

			elif row[0] == "1928":
				world_1928.append(row[0])

			elif row[0] == "1932":
				world_1932.append(row[0])

			elif row[0] == "1936":
				world_1936.append(row[0])								

			elif row[0] == "1948":
				world_1948.append(row[0])

			elif row[0] == "1952":
				world_1952.append(row[0])

			elif row[0] == "1956":
				world_1956.append(row[0])

			elif row[0] == "1960":
				world_1960.append(row[0])

			elif row[0] == "1964":
				world_1964.append(row[0])

			elif row[0] == "1968":
				world_1968.append(row[0])

			elif row[0] == "1972":
				world_1972.append(row[0])

			elif row[0] == "1976":
				world_1976.append(row[0])

			elif row[0] == "1980":
				world_1980.append(row[0])

			elif row[0] == "1984":
				world_1984.append(row[0])								

			elif row[0] == "1988":
				world_1988.append(row[0])

			elif row[0] == "1992":
				world_1992.append(row[0])

			elif row[0] == "1994":
				world_1994.append(row[0])

			elif row[0] == "1998":
				world_1998.append(row[0])

			elif row[0] == "2002":
				world_2002.append(row[0])

			elif row[0] == "2006":
				world_2006.append(row[0])

			elif row[0] == "2010":
				world_2010.append(row[0])

			elif row[0] == "2014":
				world_2014.append(row[0])

			line_count += 1

print('Number of men', len(world_1924))
print('Number of women', len(world_2014))


print('processed', line_count, 'rows of data')

x = np.arange(22)
year = [len(world_1924), len(world_1928), len(world_1932), len(world_1936), len(world_1948), len(world_1952), len(world_1956), len(world_1960), len(world_1964), len(world_1968), len(world_1972), len(world_1976), len(world_1980), len(world_1984), len(world_1988), len(world_1992), len(world_1994), len(world_1998), len(world_2002), len(world_2006), len(world_2010), len(world_2014)]

fig, ax = plt.subplots()
plt.bar(x, year, width=0.5, bottom=None, color='coral')

plt.xticks(x, ('1924', '1928', '1932', '1936', '1948', '1952', '1956', '1960', '1964', '1968', '1972', '1974', '1978', '1982', '1984', '1988', '1992', '1994', '1998', '2002', '2006', '2010', '2014'))
plt.title(" Number of medals by years (from 1924 to 2014) ", fontsize=14)

plt.show()














