import csv

f = open('ncaa2015.csv', 'rU')
reader = csv.reader(f)

scores = []

for line in reader:
	newline = []
	line = line[0].split(',')
	for boxline in line:
		score = boxline[-2:]
		team = boxline[:-2]
		newline.append(team.strip())
		newline.append(score)
	scores.append(newline)

for score in scores:
	print score

f = open("ncaa2015new.csv", "w")
writer = csv.writer(f)
for score in scores:
	writer.writerow(score)