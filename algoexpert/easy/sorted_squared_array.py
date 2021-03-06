# Solution 1
def sortedSquaredArray(array):
    for i in range(len(array)):
		el = array[i]
		array[i] = el * el

    return sorted(array)

# Solution 2
def sortedSquaredArray(array):
    res = []
	idx = 0
	for i in range(len(array)):
		el = array[i]
		el = el * el

		if len(res) == 0:
			res.append(el)
		elif el < res[idx]:
			res.insert(0, el)
			idx += 1
		else:
			res.append(el)

    return res
