tot=0
while True:
	line = raw_input()
	if line:
		inp=line.split(' ')
		if inp[0] == 'D':
			tot += int(inp[1])
		if inp[0] == 'W':
			tot -= int(inp[1])
	else:
		break
print tot

