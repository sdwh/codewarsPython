def caffeineBuzz(n):
	print(n)
	if n%3 == 0 and n % 4 == 0:
		return 'CoffeeScript'
	elif n%3 == 0:
		return 'JavaScript' if n % 2 == 0 else 'Java'
	else:
		return 'mocha_missing!'