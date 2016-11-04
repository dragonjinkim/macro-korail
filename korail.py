# -*- coding: utf-8 -*-
import time
import random
from korail2 import *
korail = Korail("ID NUMBER", "PASSWD")
korail.login()
if korail.login() == True:
	print "login success."
	count = 0
	trial = 0
	while True:
		print("trial %d\n" %trial)
#	trains1 = korail.search_train('수원','부산','20140905','120000',train_type=TrainType.KTX,include_no_seats=True)
		trains1 = korail.search_train('부산','수원','20161105','170000',train_type=TrainType.KTX,include_no_seats=True)
		trains2 = korail.search_train('부산','수원','20161105','170000',train_type=TrainType.KTX,include_no_seats=True)
#수원발권
		if len(trains1) != 0:
			for tr in trains1:
				print tr
				if tr.reserve_possible is "Y":
					seat = korail.reserve(tr)
					print "reserve OK"
					print seat
					count += 1
					break
				break
			print "\n"

#서울발권
		if len(trains2) != 0:
			for tr in trains2:
				print tr
#print tr.delay_time
				if tr.reserve_possible is "Y":
					seat = korail.reserve(tr)
					print "reserve OK"
					print seat
					count += 1
					break
				break
			print "\n"

		if count > 100:
			quit()

		trial += 1

#if len(trains2) != 0:
#if "매진" in trains2 != 0:
#seat = korail.reserve(trains2[0])
#print "success"
#print seat
#break
		time.sleep(random.random()*3)
