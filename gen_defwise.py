user_scores = []

from last_users_scored import *
for u in last_users_scored:
	entries = last_users_scored[u]
	out = ['degree0','degree1','degree2','degree3','no_definition','naive','user_id']
	for x in ['hit', 'age', 'gender', 'country']:
		out.append(x)
	for x in ['befuddle', 'besmirch', 'carom', 'debauch', 'exfoliate', 'picket', 'scotch', 'shew', 'slaver', 'twiddle']:
		for y in ['def_in', 'def_in_trained', 'def_in_untrained', 'def_out', 'level', 'trained', 'untrained']:
			if y == 'def_out' or y == 'def_in':
				continue
			out.append(x+'_'+str(y))
	user_scores.append(out)
	break


for u in last_users_scored:
	entries = last_users_scored[u]
	scores = [0 for x in range(6)]
	out = [u]
	for x in ['hit', 'age', 'gender', 'country']:
		# print x,entries[x]
		out.append(entries[x])
	for x in ['befuddle', 'besmirch', 'carom', 'debauch', 'exfoliate', 'picket', 'scotch', 'shew', 'slaver', 'twiddle']:
		# print x,entries[x]

		for y in ['def_in', 'def_in_trained', 'def_in_untrained', 'def_out', 'level', 'trained', 'untrained']:
			if y == 'def_out' or y == 'def_in':
				continue
			if y == 'level':
				# print u,entries[x]['trained'], entries[x]['untrained']
				scores[entries[x][y]] += entries[x]['trained']
				scores[5] += entries[x]['untrained']
			if y in entries[x]:
				out.append(entries[x][y])
			else:
				out.append(None)

	# for x in ['befuddle', 'besmirch', 'carom', 'debauch', 'exfoliate', 'picket', 'scotch', 'shew', 'slaver', 'twiddle']:
	# 	for y in sorted(entries[x]):
	# 		if y == 'def_out' or y == 'def_in':
	# 			continue
	# 		out.append(str(entries[x][y]))
	# print out
	# print ','.join(map(str,scores))
	if not (scores[-1]-sum(scores[:-1]))/sum(scores[:-1])>=1:
		scores[-1]/=5.0
		if not scores[-1]*2/sum(scores[:3]) >= 1:
			# print out
			user_scores.append(map(str,scores)+map(str,out))
# print len(user_scores)
# print user_scores
print 'user_scores =',user_scores



# print '\n'.join([', '.join(x) for x in user_scores])
		# print ', '.join(map(str,scores)+map(str,out))
	# print ', '.join(map(str,scores)+map(str,out))

	# print sorted(entries)


# for u in last_users_scored:
# 	entries = last_users_scored[u]
# 	out = [u]
# 	for x in ['hit', 'age', 'gender', 'country']:
# 		out.append(entries[u])
# 		'befuddle', 'besmirch', 'carom', 'debauch', 'exfoliate', 'picket', 'scotch', 'shew', 'slaver', 'twiddle']
# 	print sorted(entries)