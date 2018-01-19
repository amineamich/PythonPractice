opt=[]
l=raw_input().split(',')
for i in l:
	if int(i) % 2 != 0:
		opt.append(str(int(i)*int(i)))

print ','.join(opt)
