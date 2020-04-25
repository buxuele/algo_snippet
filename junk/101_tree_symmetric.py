class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 回顾昨天的内容，然后重写层次遍历，然后再写一下Solution,最后再做一道树的算法题
class Tree:
    def __init__(self, root):
        self.root = TreeNode(root)

    # 层次遍历, 从上到下， 一层一层的来，双向队列，前出后进
    def BFS(self, root):
        deque = [root]
        while deque:
            n = len(deque)
            for i in range(n):
                node = deque.pop(0)
                if node:
                    deque.append(node.left if node.left else None)
                    deque.append(node.right if node.right else None)

                # 如果当前节点已经是None了，那么就需要停止了，什么都不做
                # else:

    # 如何判断是否为一个堆成的树
    def solution(self, root):
        # 昨天的解法
        deque = [root]
        next_layer = []     # 保存下一层的节点
        layer = []          # 保存值
        while deque:
            for node in deque:
                if not node:
                    layer.append(None)
                    continue
                else:
                    next_layer.append(node.left)
                    next_layer.append(node.right)
                    layer.append(node.val)

            if layer != layer[::-1]:
                return False
            deque = next_layer
        return True




