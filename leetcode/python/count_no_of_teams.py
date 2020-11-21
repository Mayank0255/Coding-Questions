class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count, n = 0, len(rating)
        for j in range(1, n - 1):
            lt = sum(rating[i] < rating[j] for i in range(j))
            gt = sum(rating[j] < rating[k] for k in range(j + 1, n))
            count += lt * gt + (j - lt) * (n - j - gt - 1)
        return count
