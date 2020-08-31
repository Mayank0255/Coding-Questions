# Solution 1
def getNthFib(n):
    lastTwo = [0, 1]
	count = 3
	while count <= n:
		fib = lastTwo[0] + lastTwo[1]
		lastTwo[0] = lastTwo[1]
		lastTwo[1] = fib
		count += 1
	return lastTwo[1] if n > 1 else lastTwo[0]

# Solution 2
def getNthFib(n):
    if n == 2:
		return 1
	elif n == 1:
		return 0
	else:
		return getNthFib(n-1) + getNthFib(n-2)
