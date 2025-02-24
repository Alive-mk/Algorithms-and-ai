class Solution:
    def getDepth(self, node):
        if node is None:
            return 0
        
        leftDepth = self.getDepth(node.left)
        rightDepth = self.getDepth(node.right)
        
        if node.lrft is None and node.right is None:
            return 1 + rightDepth
        if node.left is None and node.right is None:
            return 1 + leftDepth
        
        result = 1 + min(leftDepth, rightDepth)
        
        return result
    
    def minDepth(self, root):
        if root is None:
            return 0
        
        return self.getDepth(root)
    
class Solution:
    def countNodes(self, root):
        return self.getNondesNum(root)
    
    def getNondesNum(self, cur):
        if cur is None:
            return 0
        
        leftNum = self.getNondesNum(cur.left)
        rightNum = self.getNondesNum(cur.right)
        treeNum = leftNum + rightNum + 1
        
        return treeNum