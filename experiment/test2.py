from defs import *
from defouts import *
from last_users import *
from defsums import *

dicts = {}

deflist = []

count = [0,0]

for user in last_users:
	resps = last_users[user]
	for entry in resps:
		entrydata = resps[entry]
		
		if 'def_in' in entrydata and entrydata['def_in']:
			entrydata['def_in_trained']=None
			entrydata['def_in_untrained']=None
			if entrydata['def_in'] in defsums:
				entrydata['def_in_trained']=defsums[entrydata['def_in']][0]
				entrydata['def_in_untrained']=defsums[entrydata['def_in']][1]
print 'last_users =',last_users