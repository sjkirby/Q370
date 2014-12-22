from last_resps import *
import defs

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

scores = []

for u in sorted(resps):
	ans = resps[u]
	
	# for x in sorted(ans):
	# 	print x, ans[x]
	# print
	info = [u,ans['hit']]
	ans.pop('hit')
	for x in ['age','country','gender']:
		info.append(ans[x][0])
		ans.pop(x)
	mscores = [0 for x in range(6)]+info
	for x in sorted(ans):
		if x[-1] == 'D':
			continue
		good = ans[x][0] in defs.syns[x[1:-1]]
		print x,ans[x][0],good
		if good:
			if(int(x[-1]) < 3):
				mscores[5] += 1
			else:
				mscores[int(x[0])] += 1
	scores.append(mscores)

for x in scores:
	for y in x:
		print str(y)+",",
	print

print 'scores =',scores

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