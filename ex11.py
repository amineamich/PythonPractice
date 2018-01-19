vec=[]
line=raw_input().split(',')
for i in line:
	if ( int(i)%5 == 0 ):
		vec.append(i)
print ','.join(vec)