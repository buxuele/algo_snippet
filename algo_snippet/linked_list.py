# 链表的实现及其基本操作方法


class Node:
    def __init__(self, item=None, next=None):
        self._item = item
        self.next = next

    def ___repr__(self):
        return str(self._item)


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 1

    def isEmpty(self):
        return self.length == 0

    # 尾部添加元素
    def add_tail(self, item):
        if isinstance(item, Node):
            node = item
        else:
            node = Node(item)

        if self.head == None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = node
            self.length += 1

    # 插入任意位置
    def insert_data(self, index, item):
        if self.isEmpty():
            print("empty!")
            return False
        if index < 0 or index >= self.length:
            print("index out of range!")
            return False

        insert_node = Node(item)
        node = self.head
        count = 1

        while True:
            node = node.next
            count += 1
            if count == index:
                next_node = node.next
                node.next = insert_node
                insert_node.next = next_node
                self.length += 1
                break
    # 删除数据
    def delete_data(self, index):
        if self.isEmpty():
            return False

        if index < 0 or index >= self.length:
            print("index out of range!")
            return False

        node = self.head
        count = 0
        while True:
            count += 1
            if index == count:
                node.next = node.next.next
                break
            node = node.next
        self.length -= 1

    def __repr__(self):
        if self.isEmpty():
            return False

        res = ""
        node = self.head
        while node:
            res += node._item + ""
            node = node.next
        return res


if __name__ == '__main__':
    chain = LinkedList()
    chain.add_tail("A")
    chain.add_tail("B")
    chain.add_tail("C")
    chain.add_tail("D")
    print(chain, chain.head._item, chain.length)

    chain.insert_data(2, "G")
    print(chain, chain.head._item, chain.length)

    chain.delete_data(3)
    print(chain, chain.head._item, chain.length)



