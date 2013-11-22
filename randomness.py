import random
def flip():
	st = raw_input("Write 'n' to flip a coin ")
	while (st != 'n'):
		st = raw_input("It wasn't 'n'!!! Write 'n' please ")		
	num = random.randint(1,2)
	if num == 1  :
		return "H"
	else :
		return "T"

def flip_prob():
	prob = float(raw_input("give me a probability format: '0.x' "))
	while (prob > 1 or prob <= 0)  : 
		prob = float(raw_input("Number must be between 0 and 1, again: "))
	num = random.random()
	if num <= prob  :
		print "H"
	else :
		print "T"

def multi_flip() :
	times = int(raw_input("how many times to flip a coin"))
	li= list()	
	for x in range(times): 
		li.append(flip())
	return li 


print multi_flip()
