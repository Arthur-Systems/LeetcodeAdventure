class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def delete_node(root, val):
    if not root:
        return
    if root.val < root.left:
        root.left = delete_node(root.left, val)
    if root.val > root.right:
        root.right = delete_node(root.right, val)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        succ = root.right

        while succ.left:
            succ = succ.left

        root.val = succ.val

        root.right = delete_node(root.right, succ.val)

    return root
