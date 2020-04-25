# 二叉树的左叶子之和
# 自己独立完成的 而且是只用了十几分钟，就是一个层次遍历的变形

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
执行用时 :56 ms, 在所有 Python3 提交中击败了9.20%的用户
内存消耗 :12.8 MB, 在所有 Python3 提交中击败了100.00%的用户
"""
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # 先尝试自己来写
        # 思路是 层次遍历一下，凡是起左边的，累加来
        deque = [root]
        res = 0
        while deque:
            for i in range(len(deque)):
                node = deque.pop(0)
                if node:
                    # print(node.val)
                    deque.append(node.left if node.left else None)
                    deque.append(node.right if node.right else None)
                    if node.left and node.left.left is None and node.left.right is None:
                        # print(node.left.val)
                        res += node.left.val

        # print(res)
        return res