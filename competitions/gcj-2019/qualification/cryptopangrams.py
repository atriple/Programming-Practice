# Used python to solve big integers.
# PROBLEMS : RUNTIME ERROR, TEST CASE SKIPPED. I don't know  what to do anymore...
# I will use C++ for now, but it ain't going to solve the hidden test case sadly.
import string

#prime generator >3
def primes(n): 
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]] 

alphabet = list(string.ascii_uppercase) #alphabet list

t = int(input()) #read a line with a single integer
for i in range(1, t + 1):
	n, l = [int(s) for s in input().split(" ")] # read a list of integers, 2 in this case
	encrypt_msg = [int(s) for s in input().split(" ")] 
	usedprime = []

	primelist = primes(n+1)
	
	#check the first integer in encrypt_msg
	for x in primelist :
		if encrypt_msg[0] % x == 0 :
			usedprime.append(x)
			usedprime.append(int(encrypt_msg[0]/x))
			break
	print(usedprime)
	#check the right first prime value, remove the second value
	if (encrypt_msg[0] % primelist[0] == 0) and (encrypt_msg[1] % primelist[0] == 0) :
		usedprime[0] = usedprime[1]
	
	usedprime.pop()
	print(usedprime)

	#solve the rest :
	index = 0
	for y in encrypt_msg :
		usedprime.append(int(y / usedprime[index]))
		index = index + 1

	#sorting
	sortedprime = list(set(usedprime))
	sortedprime.sort()

	'''
	THIS DOESN'T WORK IN GCJ

	#change the list into dict
	primetables = dict.fromkeys(sortedprime) #when you convert to dict with this, you will get unordered numbers.
	#to solve this, I'm going to use zip.
	
	# putting it into alphabet
	index = 0
	for z in primetables :
		primetables[z] = alphabet[index]
		index = index + 1
	'''

	ziplist = zip(sortedprime, alphabet)

	primetables = dict(ziplist)
	
	decrypt = ""
	for w in usedprime :
		decrypt = decrypt + primetables[w]
	
	print("Case #{}: {}".format(i, decrypt))