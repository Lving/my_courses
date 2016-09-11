import re
hand = open('regex_sum_303987.txt')
numlist = []
for line in hand:
	line = line.rstrip()
	if re.search('[0-9]+', line):
		y = re.findall('[0-9]+', line)
		numlist.extend(y)
x = [int(i) for i in numlist]
print sum(x)
