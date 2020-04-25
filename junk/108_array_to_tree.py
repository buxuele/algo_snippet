class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # 看了一下评论区，基本上都是使用递归，这个道题使用迭代可行吗？？？
        # 有人说是 中序遍历的逆过程，怎么理解呢？
        if not nums:
            # 这里只写一个 return 也算可以的， 表示的是结束，返回的值是 None,不是 TreeNode(None)
            return None
        else:
            middle = len(nums) // 2
            root = TreeNode(nums[middle])
            root.left = self.sortedArrayToBST(nums[:middle])
            root.right = self.sortedArrayToBST(nums[middle + 1:])
            return root

        # 下面是最初的个人尝试。
        # # root = TreeNode(None)

        # if not nums:
        #     return TreeNode(None)

        # # 使用一个临时变量来传递节点，但是 root 不能变
        # root =  TreeNode(nums.pop(0))

        # while nums:
        #     root.left = TreeNode(nums.pop(0))
        #     root = root.left
        #     if nums:
        #         root.right = TreeNode(nums.pop(0))
        #         root = root.right
        #     else:
        #         root.right = TreeNode(None)
        #         root = root.right

        #     # root.right = TreeNode(nums.pop(0))
        # return root
