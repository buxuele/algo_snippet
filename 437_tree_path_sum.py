# 这道题我觉得是属于 难的 以后需要再看看。
# 参考评论区 小坚强  的写法


class Solution:
    def __init__(self):
        self.path_sum = 0

    # 递归往下一次深度遍历根节点循环

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return self.path_sum

        self.getPathNum(root, sum)  # 每次调用这个函数的时候，改变的是 path_num的值
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)

        return self.path_sum

        # 根据当前树来找目标值，进而找到路径数量？？？

    def getPathNum(self, root: TreeNode, sum: int):
        if not root:
            return
        if root.val == sum:
            self.path_sum += 1

        # 关键在于如何理解这个 new_sum, 指的是还差多少能凑够目标值（看看下一个节点的值），
        new_sum = sum - root.val
        self.getPathNum(root.left, new_sum)
        self.getPathNum(root.right, new_sum)
