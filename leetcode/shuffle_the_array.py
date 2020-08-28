class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        list1 = nums[:n] #list of xes
        list2 = nums[n:] #list of yes
        res = []
        for i in range(len(list1)): #checking indexes in len(x and y)
            res.append(list1[i]) #fristly add element with i index from list1
            res.append(list2[i]) #then from list2
            #repeating into all indexes
        return res #return all list
