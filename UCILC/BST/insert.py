class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_node(root, val) -> TreeNode:
    if root is None:
        return TreeNode(val)
    if val < root.val:
        insert_node(root.left, val)
    if val > root.val:
        insert_node(root.right, val)
    return root


def inorder(root: Optional[TreeNode]) -> list[int]:
    out = []

    def dfs(n: Optional[TreeNode]):
        if not n:
            return
        dfs(n.left)
        out.append(n.val)
        dfs(n.right)

    dfs(root)
    return out


if __name__ == "__main__":
    root = None
    for x in [8, 5, 13, 3, 6, 11, 14, 2, 4, 7, 9, 12]:
        root = insert_node(root, x)

    print(inorder(root))  # should be sorted: [2,3,4,5,6,7,8,9,11,12,13,14]
