from collections import Iterable

# 可视化工具
import matplotlib.pyplot as plt
import networkx as nx
 
"""
二叉树的实现还是需要再理解一下
1. 如何添加数据
2. 如何遍历，哪怕是任何一种遍历
3. 下面的这个特定是普遍认同的吗，是公认的吗，还是用户按照自己的需求来指定的？？？

二叉树的一个特点是: 左边是小数，右边是大数。
二叉树每个子树都满足，大于它的左子树及其所有子节点，小于它的右子树及其所有子节点！
"""

# 下面的这中写法，而且实现了数据的可视化 参考知乎上的:
# https://zhuanlan.zhihu.com/p/35574577
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, seq=()):
        # 确保输入的参数是可迭代对象, 这个地方写的很好

        assert isinstance(seq, Iterable)
        self.root = None
        self.insert(*seq)

    #
    # 这里的 insert 是接收一个列表，然后转化为一个树结构的对象
    # 与其说是 insert,不如说是 转化，transform
    # 总之这种插入方法，我觉得是有问题的。暂时先按照这个来
    def insert(self, *args):
        if not args:
            return
        if not self.root:
            self.root = Node(args[0])
            args = args[1:]
        for i in args:
            seed = self.root
            while True:
                if i > seed.value:      # 这里为什么要比较呢？？ 大数在右，小数在左，是吗？？？
                    if not seed.right:
                        node = Node(i)
                        seed.right = node
                        break
                    else:
                        seed = seed.right
                else:
                    if not seed.left:
                        node = Node(i)
                        seed.left = node
                        break
                    else:
                        seed = seed.left

    # 为什么这样接找到最小值了呢？？？ 绝对是跟上面的插入顺序有关
    def minNode(self, seed=None):
        node = seed or self.root
        while node.left:
            node = node.left
        return node

    def maxNode(self, seed=None):
        node = seed or self.root
        while node.right:
            node = node.right
        return node

    # 通过给定值，返回对应的节点对象，如果没有则防返回None
    def find(self, item, seed=None):
        node = seed or self.root        # 修改查询的起点
        parent = None                   # 父节点
        while node:
            if item > node.value:
                parent, node = node, node.right
            elif item < node.value:
                parent, node = node, node.left
            else:
                return node, parent

    def remove(self, item):
        result = self.find(item)
        if result:
            new_node = None
            del_node, del_node_parent = result
            if del_node.value == self.root.value:
                raise ValueError("can't remove root")
            if del_node.left and del_node.right:
                right_min = self.minNode(seed=del_node.right)
                new_node = Node(right_min.value)

                if del_node.right.value == new_node.value:
                    new_node.left = del_node.left
                else:
                    new_node.left. new_node.right = del_node.left, del_node.right
                self.remove(right_min.value)

            elif del_node.left or del_node.right:
                new_node = del_node.left or del_node.right

            if del_node_parent.left and del_node_parent.left.value == del_node.vlaue:
                del_node_parent.left = new_node
            elif del_node_parent.right and del_node_parent.right.value == del_node.value:
                del_node_parent.right = new_node
            del del_node
            return
        raise ValueError("item not in this tree")



def create_graph(G, node, pos={}, x=0, y=0, layer=1):
    pos[node.value] = (x, y)
    if node.left:
        G.add_edge(node.value, node.left.value)
        l_x, l_y = x - 1 / 2 ** layer, y -1
        l_layer = layer + 1
        create_graph(G, node.left, x=l_x, y=l_y, pos=pos, layer= l_layer)
    if node.right:
        G.add_edge(node.value, node.right.value)
        rx, ry = x + 1 / 2 ** layer, y - 1
        r_layer = layer + 1
        create_graph(G, node.right, x=rx, y=ry, pos=pos, layer=r_layer)
    return G, pos


def draw(node):
    graph = nx.DiGraph()
    graph, pos = create_graph(graph, node)
    fig, ax = plt.subplots(figsize=(8, 10))
    nx.draw_networkx(graph, pos, ax=ax, node_size=300)
    plt.show()

l = [40, 20, 30, 70, 60, 75, 71, 74]
tree = BinaryTree()
tree.insert(*l)
draw(tree.root)




