#!/usr/bin/env python
import sys

reducer_num = 1 # the number of reducer

for line in sys.stdin:
	line = line.strip()
	try:
		(userid,friends) = line.split()
	except ValueError:

		continue
	friend = friends.split(',')
	friend_num = len(friend)
	
#emit friend number to reducer
	count = 1
	while(count<=reducer_num):
		print str(-count)+"\t"+str(userid)+","+str(friend_num)
		count = count + 1

#emit A and B pair , B and A pair
	i=0
	while (i<friend_num-1):
		j=i+1
		while(j<friend_num):
			print friend[i]+"\t"+friend[j]
			print friend[j]+"\t"+friend[i]
			j=j+1
		i=i+1

