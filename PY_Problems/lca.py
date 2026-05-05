class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lca(root: Node, p: Node, q: Node) -> Node:
    def dfs(node):
        if not node or node == p or node == q:
            return node
        
        left = dfs(node.left)
        right = dfs(node.right)
        
        if left and right:
            return node
        
        return left if left else right

    return dfs(root)