'''
Used python since it involve big integer.

600 851 475 143 --- 600 billion.
'''

import math
import time

n = 600851475143

'''
# Brute Force Method, not the best method, imagine you have to do 600 billion iteration.
Assume 0.1ms per iteration it will require 60 billion ms to finish, which mean 60 million seconds 
that will require 16 hour to finish. 

for i in range(init, n):
	prime = True
	if n % i == 0 : #detecting factor or not
		for j in range(2, i):
			if i % j == 0 :
				prime = False
	else :
		print("Skip")
		continue
	if prime == True :
		max = i
		print(max)

print(max)

'''