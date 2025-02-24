class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        return self.compare(root.self, root.right)
    
    def compare(self, left, right):
        if left == None and right != None: return False
        elif left != None and right == None: return False
        elif left == None and right == None: return True
        elif left.val != right.val: return False
        
        outside = self.compare(left.left, right.right)
        inside = self.compare(left.right, right.left)
        isSame = outside and inside
        return isSame
    
class Solution:
    def maxdepth(self, root):
        return self.getdepth(root)
    
    def getdepth(self, node):
        if not node:
            return 0
        leftheight = self.getdepth(node.left)
        rightheight = self.getdepth(node.right)
        height = 1 + max(leftheight, rightheight)
        return height
    
class Solution:
    def maxdepth(self, root):
        if not root:
            return 0
        
        return 1 + max(self.maxdepth(root.left), self.maxdepth(root.right))

import collections

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        
        depth = 0
        queue = collections.deque([root])
        
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return depth