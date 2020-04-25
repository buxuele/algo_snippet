# 基本的二叉树的实现


# 下面这种写法有点不清晰。舍弃了。
class Node:
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value


class Tree:
    def __init__(self, root=None):
        self.root = root

    def pre_order(self, root):
        if root is None:
            return
        else:
            print(root.value)
            self.pre_order(root.left)
            self.pre_order(root.right)

    def BFS(self, root):
        if root is None:
            return
        else:
            queue = []
            queue.append(root)
            while queue:
                currentNode = queue.pop()
                print(currentNode.value)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)