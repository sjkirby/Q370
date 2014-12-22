from last_resps import *
import defs
from hit_definitions import *

resps = last_resps

d3 = {}

for x in defs.d1:
	d3[x] = []

for u in list(resps):
	ans = resps[u]
	for title in list(ans):
		if(title[-1] == "T"):
			good =  ans[title][0] in defs.truth[title[:-1]]
			ans.pop(title)
			if(not good):
				print resps[u]
				resps.pop(u)
				break

users = {}

for u in sorted(resps):
	ans = resps[u]
	
	# for x in sorted(ans):
	# 	print x, ans[x]
	# print
	uresps = {}


	
	for x in ['age','country','gender']:
		uresps[x] = ans[x][0]
		ans.pop(x)

	for x in ['shew', 'carom', 'twiddle', 'picket', 'debauch', 'exfoliate', 'befuddle', 'slaver', 'scotch', 'besmirch']:
		uresps[x] = {}
		uresps[x]['def_in'] = None
		if x in allround[ans['hit']]:
			uresps[x]['def_in'] = allround[ans['hit']][x]
		uresps[x]['def_out'] = None
		uresps[x]['untrained'] = 0
		uresps[x]['trained'] = 0
		uresps[x]['level'] = None

	uresps['hit'] = ans['hit']
	ans.pop('hit')

	for x in sorted(ans):
		if x[-1] == 'D':
			uresps[x[:-1]]['def_out'] = ans[x]
			continue
		good = ans[x][0] in defs.syns[x[1:-1]]
		print x,ans[x][0],good
		uresps[x[1:-1]]['level'] = int(x[0])
		if good:
			if(int(x[-1]) < 3):
				uresps[x[1:-1]]['untrained'] += 1
			else:
				uresps[x[1:-1]]['trained'] += 1
	users[u] = uresps

print 'users =',users

# for u in list(resps):
# 	ans = resps[u]
# 	for title in ans:
# 		if(title[-1] == "T"):
# 			good =  ans[title][0] in defs.truth[title[:-1]]
# 			print good
# 			if(not good):
# 				resps.pop(u)
# 				break

# for x in d3:
# 	for i in range(len(d3[x])):
# 		d3[x][i] = str(d3[x][i]).encode('utf8')

# print 'd3 = ',str(d3).encode('utf8')