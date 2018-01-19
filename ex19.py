tupl=[]
while True:
	line = raw_input()
	if line:
		tupl.append(line.split(','))
	else:
		break

print(tupl)
print sorted(tupl, key=itemgetter(0,1,2))