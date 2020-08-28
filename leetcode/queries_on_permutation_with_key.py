class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = [i for i in range(1, m + 1)]

        for i in range(len(queries)):
            queries[i] = P.index(queries[i])
            temp = P.pop(queries[i])
            P.insert(0, temp)
        return queries
