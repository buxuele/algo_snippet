# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 参考知乎，其实我前几天已经先看过那篇文章了，然后才遇到这道题
        # 使用递递归，只要左右子节点，有一个存在，那么就自增1
        # 如果使用迭代来求最大深度的话，可行吗？？？
        # 评论区 派大星星星星 的答案值得再看看。

        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
