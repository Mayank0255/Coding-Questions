class Solution:
    def to_next_point(self, p1, p2):
        d1 = abs(p1[0] - p2[0])
        d2 = abs(p1[1] - p2[1])
        s1 = min(d1, d2)
        s2 = max(d1 ,d2) - s1
        return s1+s2

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points)-1):
            ans += self.to_next_point(points[i], points[i+1])
        return ans
        
