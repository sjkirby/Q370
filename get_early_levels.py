from first_users import *

dicts = {}

defouts = {}

deflist = []

for user in first_users:
	resps = first_users[user]
	for entry in resps:
		entrydata = resps[entry]
		if 'def_out' in entrydata and entrydata['def_out']:
			defi = entrydata['def_out'][0].strip().lower()
			if defi not in defouts:
				defouts[defi] = []
			defouts[defi].append((entrydata['trained'],entrydata['untrained']))

print 'defouts =',defouts
print len(defouts)