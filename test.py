def sum_of_n(n):
	res = []
	v = 0
	for i in range(abs(n)+1):
		v += i if n >= 0 else -i
		res.append(v)
	return res


print(sum_of_n(5))
print(sum_of_n(3))
print(sum_of_n(-5))
  