import sys
import random
# print sys.argv

def shuf(ls):
	return random.sample(ls,len(ls))

f = open(sys.argv[1])

csv = []

for x in f:
	csv.append(map(lambda x: x.strip(), x.split('\t')))

csv[0] = range(5) + csv[0][:-5]
lkp = {}
indx = csv[0][32:]

for y in csv[0][32:]:
	lkp[y] = []

print indx

for x in csv[1:]:
	print x[32:]
	print len(x[32:])
	print len(indx)
	for y in range(len(indx)):
		lkp[indx[y]].append(x[32+y])

defs = {}

for x in lkp:
	if x[-1] == "D":
		# print x[7:-1]
		out = []
		for y in lkp[x]:
			if(len(y) > 0):
				out.append(y)
		out = random.sample(out,10)
		defs[x[7:-1]] = out
		# for y in random.sample(out,10):
		# 	print y.lower()
		# print
for x in defs:
	print x
	print defs[x]