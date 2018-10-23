#!/usr/bin/env python

import sys
dict1 = {}  # dictionary1,store friend number of all users
list_jac = []  # list of jaccard, tmp store a set of jaccard of one user
user_last = -1  # tmp for last user in list
list_relate = []  # a list to record friend relationship of A
current_id = -100 #record the current uid, compare with the next uid
 
def record_friends(pair): # function to record friend numbers of all users
	uid, count = pair.split(",")
	uid = int(uid)
	count = int(count)
	dict1.update({uid:count})

def calculate(a,b,count): # function to calculate jaccard similarity
	if a > -1:
		a = int(a)
		b = int(b)
		count = int(count)
		a_friend_num = dict1.get(a)
 		b_friend_num = dict1.get(b)
 		jaccard = float(count)/float(a_friend_num + b_friend_num - count)
		global user_last
		if a != user_last and user_last>=0:
			top10()
		user_last = a
		tmp = [jaccard,a,b]
		list_jac.append(tmp)#record [<a,b>,similarity]in list

def top10():#funtion to find top 10 similarity of one user
	global list_jac
	list_jac.sort()
	list_jac.reverse()
	top = 0
	while top<10:
		try:
			tmp = list_jac[top]
		except Exception,mas:
			list_jac = []
			break
		a = list_jac[top][1]
		b = list_jac[top][2]
		similar = 100*list_jac[top][0]
		key = str(a)
		if key.endswith("119"):
			print "%d,%d\t%.2f%%"%(a,b,similar)
		top = top + 1
	list_jac = []

def record_relate(a,b):#function to record all of A's relationship
	a = int(a)
	b = int(b)
	global list_relate
	tmp = [a,b]
	list_relate.append(tmp)

def calculate_list():#function to sum up the same relationship of A
	global list_relate
	try:
		list_relate.sort()
		count = 1
		a = -1
		val_now = -1
		for each in list_relate:
			a = each[0]
			b = each[1]
			if b==val_now:
				count = count + 1
			elif val_now>=0 :
				calculate(a,val_now,count)
				val_now = b
				count = 1
			else:
				val_now = b
				count = 1
		calculate(a,val_now,count)
	except Exception :
		pass
# main function
for line in sys.stdin:
	line = line.strip()
	try:
		key, val = line.split('\t')
	except Exception,mas:
		continue
	uid = int(key)
	if uid > -100 and uid < 0:
		record_friends(val)
	elif uid==current_id :
		record_relate(uid,val)
	elif uid>=0 and current_id>=0:
		calculate_list()
		list_relate = []
		record_relate(uid,val)
		current_id = uid
	else:
		record_relate(uid,val)
		current_id = uid 
try:
	calculate_list()
	top10()
except Exception,mas:
	pass

