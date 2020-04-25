class Solution:

    # 评论区有种写法是使用递归来写的。
    def tree2str(self, t: TreeNode) -> str:

        if not t:
            return ""
        if not t.left and not t.right:
            return str(t.val)

        res = str(t.val)

        if t.left:
            res += "(" + self.tree2str(t.left) + ")"
        else:
            res += "()"

        if t.right:
            res += "(" + self.tree2str(t.right) + ")"

        print(res)
        return res

"""
题目的意思是子节点需要用()来包裹。
举例来说，二叉树[root,left,right]，则转换为root(left)(right)。
如果只有left为空节点，则输出root()(right)；
如果只有right为空节点则可以忽略右节点的()，输出为root(left)
"""