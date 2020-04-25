class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 与树有关的题，还是首先考虑递归。毕竟在逻辑上是最接近的

# 递归也还是需要熟练掌握的。。。
# - 考虑各自情况，需要全面
# - 留意递归函数需要传入的参数具有哪些特征
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 能否使用 一个变量，来遍历2个树，并且比较他们的值
        # 显然使用遍历的话，不适合这道题

        # 使用递归
        # 参考评论区 18960557757
        if not p and not q:
            return True
        elif p and q:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
        else:
            return False