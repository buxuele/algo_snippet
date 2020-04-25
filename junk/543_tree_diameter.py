# 对于这道题而言，下面的这2中说法都是很正确的。很好的转化。
# 直径 = 左子树树高 + 右子数树高 + 1（考虑根节点） - 1（边数=节点数-1）
# 可以将二叉树的直径转换为：二叉树的 每个节点的左右子树的高度和 的最大值。
class Solution:
    def __init__(self):
        self.nums = 0

    # 下面是如何来理解这个递归
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def length(node):
            if not node:
                return 0

            # 下面这2行不能孤立来看，而要看这个函数整体上在最终返回的是什么，
            # 返回的是什么类型的数据，在这里是 int.
            left = length(node.left)
            right = length(node.right)

            self.nums = max(self.nums, left + right)
            return max(left, right) + 1

        length(root)
        return self.nums