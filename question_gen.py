import random
random.seed()

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

defs = {'picket': 'a soldier or a group of soldiers whose duty is to guard something (such as a camp)',
'befuddle': 'to muddle or stupefy with or as if with drink',
'besmirch': 'to cause harm or damage to (the reputation of someone or something)',
'twiddle': 'to turn (something) back and forth slightly',
'debauch': 'to lead away from virtue or excellence. to corrupt by intemperance or sensuality',
'slaver': 'to allow liquid to drip out of the mouth',
'scotch': 'to put an end to (scotched rumors of a military takeover)',
'exfoliate': 'to cast off in scales, laminae, or splinters',
'shew': 'to give information that proves (something)',
'carom': 'a rebounding especially at an angle'}

words = ['befuddle', 'besmirch', 'carom', 'debauch', 'exfoliate', 'picket', 'scotch', 'shew', 'slaver', 'twiddle']

sorted_words = sorted(words)

def sample(xs):
	return random.sample(xs,len(xs))

def wordpairs(words):
	wordpairs = {}	
	for i in range(len(words)):
		neighbors = range(len(words))
		del neighbors[i]
		pairings = map(lambda x: words[x], random.sample(neighbors,3))
		wordpairs[words[i]] = pairings
	return wordpairs

answers = []
wordpairs = wordpairs(words)

lans = []
rans = []

defarr = []

for x in defs:
	defarr.append([x,defs[x]])

defarr = sample(defarr)

for y in words:
	answers = sample(syns[y])
	r = [[x] for x in answers]
	for x in wordpairs[y]:
		r = map(lambda a,b: a+[b], r, sample(syns[x]))
	r = [sample(x) for x in r]
	answers = map(lambda word,syn,i: [word+str(i),syn],[y for x in range(6)],r,range(6))
	lans += answers[:3]
	rans += answers[3:]
	truths = []
for x in truth_test:
	truths.append([x+'T',sample(truth_test[x])])
truths = sample(truths)
# print truths
lans+= truths[:2]
rans+= truths[2:]

lans = sample(lans)
rans = sample(rans)





ndefarr = sample(defarr)


def print_pages():
	import question_helpers as qh
	for er in range(5):

		print '|||||||||||||||||||||||||||NEW PAGE|||||||||||||||||||||||||||||'
		qh.set_page(2)
		qh.header()

		for x in range(0,32,4):
			qh.questionPage(lans[x:x+4])
		print

		mdefarr = ndefarr[0:er*2]+ndefarr[er*2+2:10]
		mdefarr = sample(mdefarr)
		for x in range(0,8,2):
			qh.definitions_page(mdefarr[x:x+2])
		print

		for x in range(0,32,4):
			qh.questionPage(rans[x:x+4])
		print

		mdefarr = sample(mdefarr)
		for x in mdefarr:
			qh.new_defs_page(x)
		print

		qh.demos()

		qh.thanks()

print_pages()
# for x in defarr:
# 	print x
# print

# for x in rans:
# 	print x
# print
