# Solution 1
def twoNumberSum(array, targetSum):
	nums = {}
	for num in array:
		targetNum = targetSum - num
		if targetNum in nums:
			return [num, targetNum]
		else:
			nums[num] = True
	return []

# Solution 2
def twoNumberSum(array, targetSum):
	dct = {array[i]: 1 for i in range(0, len(array))}
	for i in dct.keys():
		if dct.get(targetSum - i) == 1 and i != (targetSum - i):
			return [i, targetSum-i]
	return []

# Solution 3
def twoNumberSum(array, targetSum):
    array.sort()
	left = 0
	right = len(array) - 1

	while left < right:
		res = array[left] + array[right]
		if targetSum == res:
			return [array[left], array[right]]
		elif res < targetSum:
			left += 1
		elif res > targetSum:
			right -= 1
	return []
