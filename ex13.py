l=raw_input()
ccount=dcount=ocount=0
for c in l:
	if c.isalpha() == True:
		ccount+=1
	elif c.isdigit() == True:
		dcount+=1
	else: ocount+=1
print 'LETTERS '+str(ccount)
print 'DIGITS ' +str(dcount)		