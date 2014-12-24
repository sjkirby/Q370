import d0_data as d0
import d1_data as d1
import random

syns = {'picket': [u'lookout', u'lookout man', u'sentinel', u'sentry', u'watch', u'spotter'],
'befuddle': [u'confuse', u'bedevil', u'confound', u'discombobulate', u'inebriate', u'intoxicate'],
'besmirch': [u'defame', u'slander', u'smirch', u'denigrate', u'smear', u'sully'],
'twiddle': [u'twirl', u'swirl', u'whirl', u'fiddle with', u'go around', u'manipulate'],
'debauch': [u'corrupt', u'pervert', u'subvert', u'demoralize', u'debase', u'profane'],
'slaver': [u'drivel', u'drool', u'slabber', u'slobber', u'dribble', u'salivate'],
'scotch': [u'thwart', u'queer', u'spoil', u'foil', u'frustrate', u'baffle'],
'exfoliate': [u'break away', u'break off', u'cast off', u'chip', u'chip off', u'shed'],
'shew': [u'demonstrate', u'establish', u'affirm', u'corroborate', u'substantiate', u'support'],
'carom': [u'bounce', u'bound', u'glance', u'recoil', u'reverberate', u'ricochet']}

truth_test = {'big': ['large','dog','cat','mouse'],
'small': ['little','run','fox','house'],
'male': ['man','philosophy','prime','complex'],
'easy': ['simple','boot','russia','keyboard']}

truth_test_true = {'big': ['large'],
'small': ['little'],
'male': ['man'],
'easy': ['simple']}

ans_dict = {}

resps = [d0.responses,d1.responses]
files = ['d0filter','d1filter']

for word in syns:
	ans_dict[word] = []

for resp in d0.responses:
	for word in syns:
		if(word+'D' in resp and resp[word+'D']):
			ans_dict[word].append(resp[word+'D'])

for x in ans_dict:
	ans_dict[x] = random.sample(ans_dict[x],10)

print 'defs = ',ans_dict

