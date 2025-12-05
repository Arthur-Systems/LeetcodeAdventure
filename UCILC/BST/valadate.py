from typing import Optional


class TreeNode:
    def __init__(
        self,
        val=0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: Optional[TreeNode]) -> bool:
    def traverse(node, low, high):
        if not node:
            return True

        if not (low < node.val < high):
            return False
        return traverse(node.left, low, node.val) and traverse(
            node.right, node.val, high
        )

    return traverse(root, float("-inf"), float("inf"))


def node(val, l=None, r=None):  # tiny constructor alias to keep tests readable
    return TreeNode(val, l, r)


def run_tests():
    # 1) Empty / single
    assert isValidBST(None) is True
    assert isValidBST(node(5)) is True

    # 2) Valid BST
    #        8
    #      /   \
    #     5     13
    #    / \    / \
    #   3  6  11  14
    root_valid = node(8, node(5, node(3), node(6)), node(13, node(11), node(14)))
    assert isValidBST(root_valid) is True

    # 3) Invalid: 6 in right subtree of 10 (must be >10)
    bad = node(10, None, node(15, node(6), node(20)))
    assert isValidBST(bad) is False

    # 4) Invalid due to duplicate (strict BST)
    dup = node(5, node(3), node(5))
    assert isValidBST(dup) is False

    print("All tests passed ✅")


if __name__ == "__main__":
    run_tests()
