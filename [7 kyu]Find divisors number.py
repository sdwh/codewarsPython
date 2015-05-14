def divisors(n):
	num = 0
	for i in range(1,n+1):
		num += 1 if n%i == 0 else 0
	return num