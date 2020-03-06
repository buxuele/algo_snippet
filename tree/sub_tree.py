# python3 实现二叉树
# 最好是参考这篇再看一遍:
# https://www.cnblogs.com/maxiaonong/p/10060086.html

class Node:
    def __init__(self, element, lchild=None, rchild=None):
        self.element = element
        self.lchild = lchild
        self.rchild = rchild


class Tree:
    def __init__(self, root=None):
        self.root = root

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur_node = queue.pop()  # 拿到列表的最后一个元素，作为当前的指针节点
                if cur_node.lchild is None:
                    cur_node.lchild = node
                    return
                elif cur_node.rchild is Node:
                    cur_node.rchild = node
                    return
                else:
                    queue.append(cur_node.lchild)
                    queue.append(cur_node.rchild)

    # 广度优先
    def width_circle(self):
        if self.root is None:
            return ''
        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur_node = queue.pop()
                print(cur_node.element, end=" ")
                if cur_node.lchild is not None:
                    queue.append(cur_node.lchild)
                if cur_node.rchild is not None:
                    queue.append(cur_node.rchild)

    # 前序遍历
    def pre_order(self, node):
        if node == None:
            return
        print(node.element, end="")
        self.pre_order(node.lchild)
        self.pre_order(node.rchild)


    # 中序遍历
    def in_order(self, node):
        if node == Node:
            return
        print(node.element, end="")
        self.in_order(node.lchild)
        self.in_order(node.rchild)

    # 后序遍历












