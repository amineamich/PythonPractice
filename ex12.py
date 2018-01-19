l=[]
for i in range(1000, 3001):
	flag=False	
	for c in str(i):
		if ( int(c) % 2 != 0 ):
			flag=True
			break
	if ( flag == False ): 
		l.append(str(i))

print ','.join(l) 
				

