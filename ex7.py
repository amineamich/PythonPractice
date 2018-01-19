matr=[]
inp = raw_input().split(',')
for j in range(0, int(inp[1]), 1):
	arr=[]
	for i in range(0, int(inp[0]), 1):
		arr.append(str(i*j))
	matr.append(arr)
print matr