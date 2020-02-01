# 遍历二叉树的所有路径
# 暂时还是觉得有点难以理解。
# 这个还需要找个测试例子来测试一下实际的效果是什么样的


# 递归遍历所有的路径
def travel(node):
    if not node.left and not node.right:
        return [str(node.val)]
    left, right = [], []
    if node.left:
        left = [str(node.val) + x for x in travel(node.left)]
    if node.right:
        right = [str(node.val) + x for x in travel(node.right)]

    # 下面这个 return 的条件是什么呢？？？
    # 是 if node.left or node.right: ？？？
    return left + right


# 迭代遍历所有的路径　我觉得这种写法更好理解一些。。
def binaryTreePaths(self, root):
    if not root:
        return []

    paths = []
    # 同时保存节点和节点的值（节点经过的路径）
    stack = [(root, str(root.val))]

    while stack:
        node, path = stack.pop()

        # 如果已经到了某个叶子节点，那就把当前这条路径加入到总的路径中。
        if not node.left and not node.right:
            paths.append(path)

        if node.left:
            stack.append((node.left, path + '->' + str(node.left.val)))
        if node.right:
            stack.append((node.right, path + '->' + str(node.right.val)))

    return paths

