# 二叉树的后序遍历
# 左子树 --> 右子树 --> 根


# 递归
def post_order(root):
    if not root:
        return

    post_order(root.left)
    post_order(root.right)
    print(root.val)


# 遍历
def post_order2(root):
    stack = []
    while stack or root:
        while root:
            stack.append(root)
            # 能左就左，不能左就右
            if root.left:
                root = root.left
            else:
                root = root.right

        node = stack.pop()
        print(node.val)

        # 如果当前节点是上一节点的左子节点，则遍历右子节点
        if stack and node == stack[-1].left:
            root = stack[-1].right
        else:
            root = None





