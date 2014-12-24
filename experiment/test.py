import csv
import sys
csvfile = open('defdrive.csv')
csvreader = csv.DictReader(csvfile, delimiter=',')

ls = []

for row in csvreader:
	if row['level'] != sys.argv[1]:
		continue
	data = [row['def_in_trained'],row['def_in_untrained'],row['trained'],row['untrained']]
	data = map(float,data)
	datad = {}
	datad['left'] = round(data[1])
	datad['right'] = round(data[3])
	datad['label'] = ''
	datad['width'] = 1
	flag = True
	for x in ls:
		if x['left'] == datad['left'] and datad['right'] == x['right']:
			x['width']+=1
			flag = False
	if flag:
		ls.append(datad)
print 'var datas=',ls
