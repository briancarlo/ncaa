f = open('NCAAData_new.csv', 'r')

for line in f:
	line = line.strip()
	print "[" + line + "],"