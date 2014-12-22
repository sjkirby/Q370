from questions import *
import re

import urllib

def pad(a):
	for x in dir(a):
		print x



found = None

lastround = set()

for HITId in questions:
	question = questions[HITId]
	foundo = re.finditer('<fieldset><label>[a-z]*</label>',question)
	it = 0
	for hit in foundo:
		if it == 0:
			# print HITId
			it+=1
		# for indpair in hit.regs:
		# 	end = question[indpair[0]:].find('</fieldset>')+len('</fieldset>')
		# 	out = question[indpair[0]:indpair[0]+end]
		# 	out = out.replace('\n','').replace('\t','').replace('\r','')
		# 	wordsplits = ['<label>','</label>']
		# 	defsplits = ['<p>','</p>']
		# 	word = out[out.find(wordsplits[0])+len(wordsplits[0]):out.find(wordsplits[1])]
		# 	definition = out[out.find(defsplits[0])+len(defsplits[0]):out.find(defsplits[1])]
		# 	print [word,definition]
	if it == 0:
		if question.find('out3') == -1:
			continue
		lastround.add(HITId)
		qurl = question[question.find('https://'):question.find('</ExternalURL>')]
		f = urllib.urlopen(qurl)
		content = f.read()

		questions[HITId] = content

earlyround = {}
finalround = {}
ans = {}

found = None
for HITId in questions:
	question = questions[HITId]
	foundo = re.finditer('<fieldset><label>[a-z]*</label>',question)
	it = 0
	for hit in foundo:
		if it == 0:
			ans[HITId] = {}
			it+=1
		for indpair in hit.regs:
			end = question[indpair[0]:].find('</fieldset>')+len('</fieldset>')
			out = question[indpair[0]:indpair[0]+end]
			out = out.replace('\n','').replace('\t','').replace('\r','')
			wordsplits = ['<label>','</label>']
			defsplits = ['<p>','</p>']
			word = out[out.find(wordsplits[0])+len(wordsplits[0]):out.find(wordsplits[1])]
			definition = out[out.find(defsplits[0])+len(defsplits[0]):out.find(defsplits[1])]
			ans[HITId][word] = definition

for hit in ans:
	defs = ans[hit]
	if hit in lastround:
		finalround[hit] = defs
	else:
		earlyround[hit] = defs

print 'ans =',ans
print
print 'earlyround =',earlyround
print
print 'finalround =',finalround
print

#.find("</fieldset>")