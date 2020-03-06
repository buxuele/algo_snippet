# 二叉树的层次遍历，深入了解一下。把层数也带进去。

def solve(root):
    layers = []
    if not root:
        return layers

    # 这里的 layers 和 layer，是考虑到最终能显示出 [[], []] 这样的结果
    layer = 0
    next_layer = [root]

    while next_layer:
        layers.append([])           # 先从当前这个root层开始。这里还只是初始化一个子列表。
        layer_length = len(next_layer)

        # 这里使用了一个 for 循环，这样就把每一层很清晰地分出来了。
        for i in range(layer_length):
            node = next_layer.pop(0)
            layers[layer].append(node.val)
            if node.left:
                next_layer.append(node.left)
            if node.right:
                next_layer.append(node.right)
        layer += 1

    return layers