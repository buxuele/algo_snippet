class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
链表：
1. 第一个元素永远是 None!!! 要考虑第一个元素的Next是什么！
2. 

"""
# 参考 leetcode.cn 风会停息
# 这是一种很经典的写法，需要多看看。。。
# 还是对概念的理解有误。链表作为一种新的数据类型还是需要理解。
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(None)
        node = res
        while l1 and l2:
            if l1.val < l2.val:
                # 这里的双重赋值很有意思啊
                node.next, l1 = l1, l1.next
            else:
                node.next, l2 = l2, l2.next
            node = node.next

        if l1:
            node.next = l1
        else:
            node.next = l2
        return res.next


