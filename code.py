# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        q = collections.deque()
        q.append(root)
        cnt = 0
        while q:
            tmp = []
            for _ in range(len(q)):
                curr = q.popleft()
                tmp.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if len(result)%2 == 1:
                tmp.reverse() 
            result.append(tmp)
        return result