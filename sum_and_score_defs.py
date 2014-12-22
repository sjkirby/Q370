from defs import *
from defouts import *
from last_users import *
from defsums import * 
dicts = {}

deflist = []

count = [0,0]

defsums = {}

for x in defouts:
	scores = defouts[x]
	sums = [0,0,0]
	for y in scores:
		sums[0] += y[0]
		sums[1] += y[1]
	sums[2] = len(scores)
	defsums[x] = sums[0]/float(sums[2]),sums[1]/float(sums[2])

print 'defsums =',defsums