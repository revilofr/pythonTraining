#!/usr/bin/python2.7
# -*- coding: latin-1 -*-

import sys

#purpose of this exercice is to validate if that an input is made of only numbers
#Of course there is a lot of better way to do that, but at this step, the studdents don't have
# enough background to do it better. 

#the number to be filled by the user
number = 0
isInputOk = False #So far, we don't know other way to loop, so let's enter into the loop like that
while not isInputOk: #As long as the input is not ok
	isInputOk = True #At start, let's assume that the input is correct
	number = raw_input("What is you number ?\n ")
	index = 0
	tableSize = len(number) #As we just learnt during the training, a string is a table
	#Let's iterate over each letter of the numberTable, as long as input is correct
	while (index < tableSize) and (isInputOk == True):
		if not number[index] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
			print "You just typed a wrong character : " + number[index]
			isInputOk = False
		index += 1
print "Your number is :" + number
