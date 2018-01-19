l=raw_input()
d={"UPPER":0, "LOWER":0}
for c in l:
	if c.isalpha():
		if c.isupper():
			d["UPPER"]+=1
		else: d["LOWER"]+=1
	else: pass
print "UPPER CASE", d["UPPER"]
print "LOWER CASE", d["LOWER"]

