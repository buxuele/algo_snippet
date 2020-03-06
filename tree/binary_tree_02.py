# 二叉树的其他写法
#

# see https://blog.csdn.net/liangjiubujiu/article/details/82811226
class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root



    # 添加元素。一切都是从这里开始的。到底是如何添加元素的？
    # 下面是一次添加一个元素
    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return

        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur_node = queue.pop()
                if cur_node.left is None:
                    cur_node.left = node
                    return
                elif cur_node.right is None:
                    cur_node.right = node
                    return
                else:
                    queue.append(cur_node.left)
                    queue.append(cur_node.right)

    # 把一个列表中的所有元素，添加到一个二叉树上，下面这种写法很简单的。
    # see https://www.jianshu.com/p/7cf4aaf4f843
    def generate_tree(self, my_list):
        if my_list:
            node = Node(my_list.pop(0))
            node.left = self.generate_tree(my_list)
            node.right = self.generate_tree(my_list)
        else:
            return my_list.pop(0)
        return node


    def pre_order(self, root):
        res = []
        if root:
            res.append(root.value)
            res.append(root.left)
            res.append(root.right)
        return res












