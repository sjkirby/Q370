import csv
import sys
spamreader = ''
spamwriter = csv.writer(open('out.csv','w'))

keys = set()

responses = []

def pd(d):
	for x in d:
		print x, d[x]

for fn in sys.argv[1:]:
	with open(fn,'rb') as csvfile:
		spamreader = csv.DictReader(csvfile)
		for row in spamreader:
			for x in row:
				keys.add(x)
			for x in list(row):
				if 'Answer.' not in x:
					row.pop(x, None)
			for x in list(row):
				row[x.replace('Answer.','')] = row[x]
				row.pop(x)
			responses.append(row)

print 'responses =', responses

# print '\n'.join(sorted(keys))