"""105. Construct Binary Tree from Preorder and Inorder Traversal
Time Complexity:O(n)
Space Complexity: O(n)

Approach: the first value in preorder is the root. find the index of the root value in inorder. In inorder everything on left is left subtree and everything on the right is right subtree."""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder and not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root
        