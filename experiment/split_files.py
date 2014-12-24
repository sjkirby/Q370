import sys
import os

sep = '|||||||||||||||||||||||||||NEW PAGE|||||||||||||||||||||||||||||'

f = open('out.html')

i = 0

f2 = open('count')
arr = []
for x in f2:
	arr.append(x.strip())

o2 = open('count','w')

o2.write(str(int(arr[0])+1)+'\n')

o = open('out'+arr[0]+str(i)+'.html','w')
for x in f:
	if(sep in x):
		
		o = open('out'+arr[0]+str(i)+'.html','w')
		i+=1
		continue
	o.write(x)

os.system('mv out?*.html experiment/site')