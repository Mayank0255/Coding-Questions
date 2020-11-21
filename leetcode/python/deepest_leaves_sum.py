# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        frontier = [root]
        res = 0
        while frontier:
            nxt = []
            for u in frontier:
                if u.left:
                    nxt.append(u.left)
                if u.right:
                    nxt.append(u.right)
            if not nxt:
                break
            frontier = nxt
        return sum([u.val for u in frontier])
