# 二叉树的层次遍历，深入了解一下。把层数也带进去。
# 参看官网题解。

def solve(root):
    layers = []
    if not root:
        return layers

    layer = 0
    deque = [root]
    while deque:
        layers.append([])           # 先从当前这个root层开始。这里还只是初始化一个子列表。
        layer_length = len(deque)

        # 这里使用了一个 for 循环，这样就把每一层很清晰地分出来了。
        for i in range(layer_length):
            node = deque.pop(0)
            layers[layer].append(node.val)
            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)
        layer += 1

    return layers




