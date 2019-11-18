# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def traverse_preOrder(self, a, a_list):
        a_list.append(a.val)
        
        if a.left != None:
            self.traverse_preOrder(a.left, a_list)
        
        if a.right != None: 
            if a.left == None:
                a_list.append(None)
            self.traverse_preOrder(a.right, a_list) 
        
    
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if (p == None and q == None):
            return True
        elif p == None:
            return False
        elif q == None:
            return False
        
        p_list=[]
        self.traverse_preOrder(p, p_list)
        
        q_list=[]
        self.traverse_preOrder(q, q_list)
        
        if len(p_list) == len(q_list):
            if (p_list == q_list):
                return True
            return False    
        return False
