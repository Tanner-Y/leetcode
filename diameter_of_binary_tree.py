# https://leetcode.com/problems/diameter-of-binary-tree/
'''
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 

          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
'''

# 36ms runtime beats 98.56% of Python3 submissions 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        def traverse(node):
            if not node: return 0
            left_path = right_path = 0
            p1, p2 = traverse(node.left), traverse(node.right)
            self.diameter = max([p1+p2,self.diameter])
            return 1+ max([p1,p2])
        traverse(root)
        return self.diameter