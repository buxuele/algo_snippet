# author: fanchuangwater@gmail.com
# date: 2020/5/10 下午8:39
# 目的: 官方题解2中Java的写法，试图用python来改写一下，顺便加深对这种思路的理解


class Solution:

    def __init__(self):
        self.parent = {}    # 这个字典保存的是每个节点与其父节点之间的关系。parent = {current_node: father_node}
        self.visited = set()

    def dfs(self, root):
        if root.left:
            self.parent[root.left.val] = root
            self.dfs(root.left)

        if root.right:
            self.parent[root.right.val] = [root]
            self.dfs(root.right)

    def lowestCommonAncestor(self, root, p, q):
        self.dfs(root)      # 这里是先把整个树都遍历一下，保存每个节点与其父节点的相对关系
        while p:
            self.visited.add(p.val)
            p = self.parent.get(p.val)

        #　下面是检查　q
        while q:
            if q.val in self.visited:
                return q
            q = self.parent.get(q.val)

        return q







