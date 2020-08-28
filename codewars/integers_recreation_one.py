import math

def list_squared(m, n):
    result = []
    for num in range(m, n + 1):
        divisors = set()
        for i in range(1, int(math.sqrt(num)+1)):
            if num % i == 0:
                divisors.add(i**2)
                divisors.add(int(num/i)**2)
        total = sum(divisors)
        sr = math.sqrt(total)
        if sr - math.floor(sr) == 0:
            result.append([num, total])
    return result
