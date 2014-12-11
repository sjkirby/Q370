import json
import urllib2

f = open('random_list_filter')

arr = []

for x in f:
	arr.append(x.strip())

def countTerms(data):
	out = 0
	for x in data:
		if('verb' in x):
			out += countTerms(data['verb'])
		if('noun' in x):
			out += countTerms(data['noun'])
		if('syn' in x):
			out += len(data['syn'])
	return out

def prh(data):
	for x in data:
		if('verb' in x):
			print ' ',x
			prh(data['verb'])
		if('noun' in x):
			print ' ',x
			prh(data['noun'])
		if('syn' in x):
			print data['syn']

def pr(count,word,data):
	if(count >= 10):
		print word,count
		prh(data)
		print
	

for x in range(50,100):
	try:
		data = json.load(urllib2.urlopen('http://words.bighugelabs.com/api/2/e2401272d23710aacafb7e435083a40f/%s/json'%arr[x]))
		pr(countTerms(data),arr[x],data)
	except:
		pass

