# 递归
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)


"""
对于中序遍历而言，实际遍历的顺序是这样的。。

            1
           / \ 
          2    3 
        /  \  /  \ 
       4   5  6   7 
       
要求输出的顺序是 4 2 5 1 6 3 7
所以，中序遍历的本质是:  ？？？ 再查查看
左　---> 左　-----> 根　-------> 右



"""

# 迭代　这种写法是正确的，但是怎么来理解呢。。。
# 我觉得是需要再找几个例子对比看看。。。
def in_order(root):
    stack = []          # 　保存的是节点，不是节点的值
    while stack or root:

        # 确保先把最左边的节点都加入栈　
        while root:
            stack.append(root)
            root = root.left
        # 此时改变的是 root 的指向，
        root = stack.pop()
        print(root.val)
        root = root.right


