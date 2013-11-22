def palindrome()  :
	a  = raw_input("give me a word")
	b = a[::-1]
	if a == b   :
		print "True"
	else   : 
		print "False" 
palindrome()	