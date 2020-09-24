# Solution 1
def maxProfitWithKTransactions(prices, k):
    if not len(prices):
		return 0
	profits = [[0 for d in prices] for t in range(k + 1)]
	for t in range(1, k + 1):
		maxThusFar = float("-inf")
		for d in range(1, len(prices)):
			maxThusFar = max(maxThusFar, profits[t - 1][d - 1] - prices[d - 1])
			profits[t][d] = max(profits[t][d - 1], maxThusFar + prices[d])
	return profits[-1][-1]

# Solution 2
def maxProfitWithKTransactions(prices, k):
    if not len(prices):
		return 0
	evenProfits = [0 for d in prices]
