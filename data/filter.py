import d0_data as d0
import d1_data as d1

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

resps = [d0.responses,d1.responses]
files = ['d0filter','d1filter']

for i in range(len(files)):
	resp = resps[i]
	for resp_dict in list(resp):
		for word in truth_test_true:
			if resp_dict[word+'T'] not in truth_test_true[word]:
				resp.remove(resp_dict)
				break
	with open(files[i]+'.py','wb') as f:
		f.write('responses = ')
		f.write(str(resp))
		f.write('\n')
