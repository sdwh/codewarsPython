def run_length_encoding(s):
	if len(s) == 0:
		return []
	res = []
	char = s[0]
	count = 1
	for c in s[1:]:
		if char == c:
			count += 1
		else:
			res.append([count,str(char)])
			char = c
			count = 1
	res.append([count,str(char)])
	return res



print(run_length_encoding('hello world'))
# [[1,'h'],[1,'e'],[2,'l'],