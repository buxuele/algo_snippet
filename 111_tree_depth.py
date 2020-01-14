# 这道题，需要先尝试自己来写一下。
# 1. 如果遍历这个树的所有元素呢???
# 2. 使用层次遍历，宽度优先？？？

# 官方的解法有点复杂，看看其他写法

# 官方解法1: 递归
class Solution1:
    def minDepth(self, root):
        if not root:
            return 0

        children = [root.left, root.right]
        if not any(children):       # 表示左右子节点都不存在，只有一个root节点
            return 1

        min_depth = float('inf')    # 表示一个正无穷的数字
        for c in children:
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        return min_depth + 1


class Solution2:
    def minDepth(self, root):
        if not root:
            return 0

        else:
            stack, min_depth = [(1, root), ], float('inf')

        while stack:
            depth, root = stack.pop()
            children = [root.left, root.right]
            if not any(children):
                min_depth = min(depth, min_depth)
            for c in children:
                if c:
                    stack.append((depth + 1, c))

        return min_depth


from collections import deque

class Solution3:
    def minDepth(self, root):
        if not root:
            return 0

        else:
            node_deque = deque([(1, root),])

        while node_deque:
            depth, root = node_deque.popleft()
            children = [root.left, root.right]
            for c in children:
                if c:
                    node_deque.append((depth+1, c))

