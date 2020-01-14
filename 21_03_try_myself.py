class  NodeList:
    def __init__(self, val=None, _next=None):
        self._val = val
        self.next = _next

class Solution:
    def mergeTwoLists(self, l1, l2):
        res = NodeList(None)

        node = res
        while l1 and l2:
            if l1.val < l2.val:
                node.next, l1 = l1, l1.next
            else:
                node.next, l2 = l2, l2.next
            node = node.next

        if l1:
            node.next = l1
        else:
            node.next = l2

        return res.next





