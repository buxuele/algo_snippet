# 二叉树的层次遍历


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 到这一步，可以深切地感受一下，队列啊，栈的作用了：
# 一般的遍历，是在一个固定的范围内的查找，或者是其他计算。
# 而现在遍历，既有删除，又有添加，整个遍历的范围是变化的。这个才是难点。
# 所以需要动态地去理解整个遍历或是查找的过程
class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    #　层次遍历 需要用到一个双向队列来删除头部，并且添加尾部
    def layer_scan(self, root):
        deque = [root]
        while deque:
            for i in range(len(deque)):
                node = deque.pop(0)
                if node:
                    print(node.value)
                    # 如果存在子节点就添加子节点，如果不存在就添加None
                    deque.append(node.left if node.left else None)
                    deque.append(node.right if node.right else None)


def BFS(root):
    queue = [root]
    while queue:
        n = len(queue)
        for i in range(n):
            q = queue.pop(0)
            if q:
                print(q.val)
                queue.append(q.left if q.left else None)
                queue.append(q.right if q.right else None)

