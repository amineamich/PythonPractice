output=[]
d=dict()
for i in range(1, int(raw_input()) +1):
	output.append(str(i)+": "+str(i*i))
	d[i]=i*i
print '{' + ', '.join(output) + '}'
print d