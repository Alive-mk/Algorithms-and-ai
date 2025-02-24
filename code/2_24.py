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
        if not cur:
            return 0
        
        leftNum = self.getNondesNum(cur.left)
        rightNum = self.getNondesNum(cur.right)
        treeNum = leftNum + rightNum + 1
        
        return treeNum
    
class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    

class Solution:
    def isBalanced(self, root):
        if self.get_height(root) != -1:
            return True
        else:
            return False
        
    def get_height(self, root):
        if not root:
            return 0
        if (left_height := self.get_height(root.left)) == -1:
            return -1
        if(right_height := self.get_height(root.right)) == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        else:
            return 1 + max(left_height, right_height)
        
class Solution:
    def combine(self, n, k):
        result = []
        self.backtracking(n, k, 1, [], result)
        return result
    
    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        
        for i in range(startIndex, n + 1):
        # for i in range(startIndex, n - (k - len(path)) + 2):
            path.append(i)
            self.backtracking(n, k, i + 1, path, result)
            path.pop()
            

