def divisor(n) :
	for a in range(int(n))  : 
		if n % (1+a) == 0 : 
			print a+1

if __name__=="__main__"   :
	y=int(raw_input("give me a number"))
	divisor(y)
