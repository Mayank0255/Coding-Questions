def numberOfWaysToMakeChange(n, denoms):
    ways = [0 for i in range(n + 1)]
	ways[0] = 1
	for deno in denoms:
		for amt in range(1, n + 1):
			if deno <= amt:
				ways[amt] += ways [amt - deno]
	return ways[n]
		
