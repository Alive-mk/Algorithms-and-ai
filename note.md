```python3
class Solution:
def preordertraversal(self, root:TreeNode) -> list[int]:
	if not root:
		return []
	stack = [root]
	result = []
	node = stack.pop()
	result.append(node.val)
	if node.right:
		stack.append(node.right)
	if node.left:
		stack.append(node.left)
	return result
# 迭代方法实现先序遍历，由于是中左右，所以访问完本节点后，如果本节点的右节点不为空需要先把右节点压入栈表示后访问右节点。
```

```python3
def inordertraversal(dels, toot):
	if not root:
		return []
	stack = []
	result = []
	cur = root
	whilr cur or stack:
		if cur:
			cur = cur.left
		else:
			cur = stack.pop()
			result.append(cur.val)
			cur = cur.right
	return result
# 迭代方法实现中序遍历，由于是左中右，所以需要一直访问到左子树的最底部再处理节点，不能直接处理，访问顺序和处理顺序虽然都是左中右，但是不是同步的。
```

```python3
def postordertraversal(self, root:TreeNode):
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
# 迭代方法实现后序遍历，由于是左右中，逆序就是中右左，所以只需要在线序的基础上把左子树先压入栈即可，最后result再逆序即可。
```

```python3
def levelordertraversal(self, root:TreeNode):
	if not root:
		return
	
	levels = []
	
	def traverse(node, level):
		if not node:
			return
		if len(levels) == level:
			levels.append([])
		levels[level].append(node.val)
		traverse(node.left, level+1)
		traverse(node.right, level+1)
		
	traverse(root, 0)
	return levels
# 递归方法实现层序遍历，当len(levels)等于当前的level时就需要为该level新开一层。
```

```python3
def invertTree(self, root:TreeNode):
    if not root:
        return None
    self.left, self.right = self.right, self.left
    invertTree(self.left)
    invertTree(self.right)
    return root
# 递归的方法，先序中序和后序类似。
```

```python3
import collections
class Solution:
	def maxDepth(self, root):
		if not root:
			return 0
			
		depth = 0
		queue = collections.deque([root])
		
		while queue:
			depth += 1
			for _ in len(queue):
				node = queue.popleft()
				if node.left:
					queue.qppend(node.left)
				if node.right:
					queue.qppend(node.right)
			
		return depth
```

```python3
:=
海象运算符，表示将右侧的值赋给左侧的变量并且返回右侧的值。
```

平衡二叉树，每个节点的左右子树的高度差都不超过1。

