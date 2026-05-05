class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_target(root, k):
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)

    def two_sum(sorted_list, target):
        left, right = 0, len(sorted_list) - 1
        while left < right:
            current_sum = sorted_list[left] + sorted_list[right]
            if current_sum == target:
                return True
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return False

    sorted_values = inorder(root)
    return two_sum(sorted_values, k)

# Test
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

k = 9
print(find_target(root, k))