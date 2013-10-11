#def divisors (n,num) :
#	if n % (num+1)==0 :
#		print num+1
#
#n=int(raw_input("give me number"))
#divisors (n,10) 

def divisor(n) :
	for a in range(int(n))  : 
		if n % (1+a) == 0 : 
			print a+1

y=int(raw_input("give me a number"))
divisor(y)
