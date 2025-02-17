class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root:TreeNode):
        if not root:
            return []
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            if node.right:
                stack.append(node.right)
                
            if node.left:
                stack.append(node.left)
                
        return result 
    
    def inorderTraversal(self, root:TreeNode):
        if not root:
            return []
        
        stack = []
        result = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left 
            else:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right
        return result  
    
    def postorderTraversal(self, root:TreeNode):
        if not root:
            return []
        
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]
                