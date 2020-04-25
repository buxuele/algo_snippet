import collections

# 还是使用最基础，最原始的思路，暂时先不用递归
# 下面这种写法失败了，　
# 最下面的解法2成功了，为什么呢？？？ 就多了一行 “for _ in range(len(d)): ”
# 这是，我做的跟树有关的第一道题。总之很生疏。。。



class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        ans = 0
        d = collections.deque()
        d.append(root)
        while d:
            ans += 1

            node = d.popleft()
            if node.left is None and node.right is None:
                return ans
            if node.left:
                d.append(node.left)
            if node.right:
                d.append(node.right)


class Solution2:
    def minDepth(self, root):
        if not root:
            return 0
        ans = 0
        d = collections.deque()
        d.append(root)
        while d:
            ans += 1

            for _ in range(len(d)):

                node = d.popleft()
                if node.left is None and node.right is None:
                    return ans
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
