import csv

# f = open('ncaa2011.csv', 'rU')
# reader = csv.reader(f)

# scores = []

# for line in reader:
# 	newline = []
# 	line = line[0].split(',')
# 	for boxline in line:
# 		score = boxline[-2:]
# 		team = boxline[:-2]
# 		newline.append(team.strip())
# 		newline.append(score)
# 	scores.append(newline)

# for score in scores:
# 	print score

# f = open("ncaa2011new.csv", "w")
# writer = csv.writer(f)
# for score in scores:
# 	writer.writerow(score)

f = open('ncaa2011new.csv', 'rU')
reader = csv.reader(f)

for line in reader:
	line[3] = str(line[3])
	line[4] = str(line[4])
	line[5] = str(line[5])
	print "[" + ",".join(line[0:3]) + ',"' + line[3] + '","' + line[4] + '","' + line[5] + '"],'


