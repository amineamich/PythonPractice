lines = []
while True:
    line = raw_input()
    if line:
        lines.append(line.upper())
    else:
        break
text = '\n'.join(lines)
print text