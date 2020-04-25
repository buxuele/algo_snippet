# 此处应该是命名上差异，暂时理解为 Node
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        #
        # index1 = 0
        # index2 = 0
        res = ListNode(None)    # 初始化一个新的链表

        # 下面是比较2个元素的值。
        list1 = []
        list2 = []

        temp_node1 = ListNode(None)
        while l1.next:
            # 开始第一个
            temp_node1.val = l1.val
            list1.append(temp_node1.val)
            # 然后应该是下一个了
            temp_node1 = l1.next

        temp_node2 = ListNode(None)
        while l1.next:
            temp_node2.val = l2.val
            list2.append(temp_node2.val)
            temp_node2 = l2.next


        list3 = sorted(list1 + list2)

        for i in range(len(list3)):
            if i < len(list3) - 1:

                res.val = list3[i]
                res.next = list3[i+1]
            else:
                res.val = list3[-1]
                res.next = None


