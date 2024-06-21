# Construct Binary Tree from Preorder and Inorder Traversal

**Description:**

Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal of a binary tree and `inorder` is the inorder traversal of the same tree, construct and return the binary tree.

We're using LeetCode's provided TreeNode object for the nodes of the binary tree.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

**Example:**

```text
#         1
#       /    \
#      2      3
#     / \    / \
#    4   5  6   7
#   /
#  8

Input: preorder = [1,2,4,8,5,3,6,7], inorder = [8,4,2,5,1,6,3,7]
Output: [1,2,3,4,5,6,7,8,None,None,None,None,None,None,None]
```

## Overview

The logic of our solution is as follows:

- We know that the first item in `preorder` is the current head node. `1`
- If we find that item in `inorder`, we can figure that it has items to its left or right.
- Its left item will be the next item in `preorder`. `2`
- Its right item can be found by looking at our item's `1` `inorder` left neighbor `5`, finding that value in `preorder` and then looking at its right neighbor. `3`
- We can create a new set of these lists to run on our new head node with the same logic to find the bottom nodes.

```python
# With 1 as the head node.
preorder = [1, 2, 4, 8, 5, 3, 6, 7]
inorder = [8, 4, 2, 5, 1, 6, 3, 7]
# Now with 2 as the head node.
new_preorder = [2, 4, 8, 5]
new_inorder = [8, 4, 2, 5]
```

```python
def build_tree_1(self, preorder: list[int], inorder: list[int]) -> TreeNode:
    """
    Returns the binary tree of a given preorder and inorder traversal representation of the tree.

    Args:
        `preorder`: A list of integers that represents the preorder traversal of a given binary tree.
        `inorder`: A list of integers that represents the inorder traversal of a given binary tree.
    Returns:
        `TreeNode`: A ListNode object that is the head of a created binary tree from these descriptions.
    """

    head = TreeNode(preorder[0], None, None)

    # If there are numbers to the left of our number in "inorder"
    if len(inorder[: inorder.index(preorder[0])]) > 0:
        head.left = TreeNode(preorder[1], None, None)
        new_inorder = inorder[: inorder.index(preorder[0])]
        new_preorder = preorder[1 : 1 + len(new_inorder)]
        self.recursive_builder(new_preorder, new_inorder, head.left)
    # If there are numbers to the right of our number in "inorder"
    if len(inorder[inorder.index(preorder[0]) + 1 :]) > 0:
        new_inorder = inorder[inorder.index(preorder[0]) + 1 :]
        new_preorder = preorder[-len(new_inorder) :]
        head.right = TreeNode(new_preorder[0], None, None)
        self.recursive_builder(new_preorder, new_inorder, head.right)

    return head

def recursive_builder(
    self, preorder: list[int], inorder: list[int], new_node: TreeNode
):
    """Recursively builds a node tree given a pre-ordered and inorder set of lists of a binary tree."""

    # If there are numbers to the left of our number in "inorder"
    if len(inorder[: inorder.index(preorder[0])]) > 0:
        new_node.left = TreeNode(preorder[1], None, None)
        new_inorder = inorder[: inorder.index(preorder[0])]
        new_preorder = preorder[1 : 1 + len(new_inorder)]
        self.recursive_builder(new_preorder, new_inorder, new_node.left)
    # If there are numbers to the right of our number in "inorder"
    if len(inorder[inorder.index(preorder[0]) + 1 :]) > 0:
        new_inorder = inorder[inorder.index(preorder[0]) + 1 :]
        new_preorder = preorder[-len(new_inorder) :]
        new_node.right = TreeNode(new_preorder[0], None, None)
        self.recursive_builder(new_preorder, new_inorder, new_node.right)

    return
```

## Tests

### Unit Testing

We implemented unit-tests for this problem with `import unittest`. We designed them for code-coverage, testing edge-cases, and confidence in robustness. We checked for:

- Simple example
- One item at bottom level
- A full tree of depth 4
- Only right children
- Only left children
- One node in tree
- Two nodes in tree
- Incorrect check to make sure not always throwing true

We also wrote a separate method in `print_tree_as_list.py` for outputting the built node tree as represented by a list, for testing comparisons.

### Code Coverage

We received 100% code coverage on each tested method from the unit-test using the `coverage.py` tool.

```PowerShell
> coverage run unit_test.py
> coverage html
> coverage report -m 
Name                                     Stmts   Miss  Cover   Missing
----------------------------------------------------------------------
construct_binary_tree_from_preorder.py      27      0   100%
other_solution.py                           21      0   100%
print_tree_as_list.py                       23      0   100%
test_cases.py                               33      0   100%
tree_node.py                                 5      0   100%
unit_test.py                                58      0   100%
----------------------------------------------------------------------
TOTAL                                      167      0   100%
```

### Memory Usage Testing

I used `tracemalloc` to look at peak memory block usage during the running of my solution `build_tree_1` and another person's solution `build_tree_2`. This is tested on a binary tree of depth 4 `test_2`.

Memory blocks used:

- `build_tree_1()`: 2784 blocks
- `build_tree_2()`: 2040 blocks

### Process Time Testing

I used `timeit` to isolate the individual functions on the same input. My solution is 5% slower than the other.

- `build_tree_1()`: 3.112 x 10^-6 sec
- `build_tree_2()`: 2.993 x 10^-6 sec

## Reflections

In effort to optimize, I'd bet there's a clever way to iterate through these lists so that we don't have to clip them and call on them so much. I'm happy with my solution's readability.

Writing the method for outputting the node tree as a list for testing allowed me to build a nice test suite before submitting the answer, in checking robustness on my own rather than leaning on LeetCode.

## Solution Variations

This solution is uses a different sort of recursion logic and sets up an initial dictionary for relation of `inorder` and `preorder`. I'm not sure what they're doing with `i` and `j` incrementing and decrementing. I stepped through it in a debugger and couldn't figure what their thought was.

```python
# Someone else's solution
class Solution:
    def recursion(self, i, j):
        if i > j:
            return None

        root_val = self.preorder[self.r]
        self.r += 1
        split_index = self.inorder_index[root_val]

        left = self.recursion(i, split_index - 1)
        right = self.recursion(split_index + 1, j)

        root = TreeNode(root_val, left, right)
        return root

    def build_tree_2(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        self.inorder_index = {v: i for i, v in enumerate(inorder)}
        self.inorder = inorder
        self.preorder = preorder
        self.r = 0
        i = 0
        j = len(inorder) - 1

        result = self.recursion(i, j)
        return result
```
