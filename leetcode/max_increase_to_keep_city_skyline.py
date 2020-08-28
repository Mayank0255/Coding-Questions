class Solution:
    def maxIncreaseKeepingSkyline(self, G: List[List[int]]) -> int:
        M, N, R, C = len(G), len(G[0]), [max(r) for r in G], [max(c) for c in zip(*G)]
        return sum(min(R[i],C[j]) - G[i][j] for i,j in itertools.product(range(M),range(N)))
        
