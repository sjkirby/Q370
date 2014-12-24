from user_scores import *

names = ['befuddle', 'besmirch', 'carom', 'debauch', 'exfoliate', 'picket', 'scotch', 'shew', 'slaver', 'twiddle']
out = [['degree0','degree1','degree2','degree3','no_definition','naive','user_id','hit','age','gender','country','word','def_in_trained','def_in_untrained','level','trained','untrained']]


for x in user_scores[1:]:
	for i in range(11,61,5):
		out.append(x[0:11]+[names[(i-11)/5]]+x[i:i+5])
for i in range(len(out)):
	if 'None' in out[i]:
		out[i] = out[i][0:-5]+['']*5
print '\n'.join([','.join(x) for x in out])