gpass=[]
def containsNumber(inpStr):
	return any(char.isdigit() for char in inpStr)

def containsLetter(inpStr):
	return any(char.isalpha() for char in inpStr)

def containsCharacter(inpStr):
	return any(not char.isalnum() for char in inpStr)

def containsUpper(inpStr):
	return any(char.isupper() for char in inpStr)

def checkLength(inpStr):
	if len(inpStr) >= 6 and len(inpStr) <= 12:
		return True
	else: return False

passw=raw_input().split(',')
for p in passw:
	if containsNumber(p)==True and containsUpper(p)==True and containsLetter(p)==True and containsCharacter(p)==True and checkLength(p)==True:
		gpass.append(p)
print ','.join(gpass)