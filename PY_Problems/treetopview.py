class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def top_view(root):
    if root is None:
        return

    top_view_map = {}

    queue = [(root, 0)]

    while queue:
        node, hd = queue.pop(0)

        if hd not in top_view_map:
            top_view_map[hd] = node.data

        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))

    for key in sorted(top_view_map):
        print(top_view_map[val], end=' ')


