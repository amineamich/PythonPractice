def fctor(x):
	fct = 1
	if ( x == 0 ):
		return 1
	else:
		for i in range(x,1,-1):
			fct *= i
	return fct
print fctor(int(raw_input()))