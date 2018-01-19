import math

def calc_form(d):
	c=50
	h=30
	return math.sqrt((2*d*c)/h)

d_list=raw_input().split(',')

output=[]
for i in range(0, len(d_list)):
	output.append(str(int(calc_form(int(d_list[i])))))

print ','.join(output)

