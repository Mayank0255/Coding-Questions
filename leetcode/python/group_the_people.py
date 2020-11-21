class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        answer=[]

        _dict_=collections.defaultdict(list)
        for idx,i in enumerate(groupSizes):
            _dict_[i].append(idx)

        for key, lst in _dict_.items():
            for idx in range(0, len(lst), key):
                answer.append(lst[idx:idx + key])
        return answer
