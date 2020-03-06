#　二叉树的　先序遍历
#  重点是理解具体的遍历过程。
#  root --> left --> left --> right


# 递归
def pre_order_01(root):
    if not root:
        return

    print(root.val)
    # 这里是先把 root的左子树先执行完，之后再执行右子树
    pre_order_01(root.left)
    pre_order_01(root.right)


# 迭代，下面这2中写法其实是一样的。在实际运行中，结果是一样的。
def pre_order_02(root):
    stack = [root]
    while stack:
        s = stack.pop()     # 这里拿到的是最后一个元素

        # 这一行可以省略吗？ 答案是不可以的。
        # 因为当前这个节点有可能是None，null
        if s:
            print(s.val)
            # 这里是先把右的元素压入栈中，可以保证右边的元素是后出栈的

            # 这里怎么知道有没有　right, 和　left 呢？？？ 所以这种写法是不够完善的。
            # 在实际的运行中，如果左右孩子没有的话，是不会添加上的。
            stack.append(s.right)
            stack.append(s.left)


# 迭代的另一中写法
def pre_order_03(root):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)



















