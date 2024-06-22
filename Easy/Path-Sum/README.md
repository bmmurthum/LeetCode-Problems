# Path Sum

**Description:**

Given the `root` of a binary tree and an integer `target_sum`, return `True` if the tree has a root-to-leaf path such that adding up all the values along the path equals `target_sum`.

A leaf is a node with no children.

**Example:**

```text
#         5*
#       /    \
#      4*     8
#     / \    / \
#    11*    13  4
#   /  \         \
#  7    2*        1

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], target_sum = 22
Output: True
```

```python
# We're using LeetCode's provided TreeNode object for the nodes of the binary tree.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

## Overview

Our solution has a start method `has_path_sum_1()` that does initial setup and handles the empty-tree edge case, then calls a recursive function `recursive_search()` on the `root` node to look for our condition to be true.

1. `recursive_search()` first adds its value to the total.
2. It then check if its a leaf, if it is it checks if its sum of path `cur_total` is equal to our desired sum `self.target_sum`.
    - If this is true, we return `True`, otherwise `False`.
3. If we have a child, we call this function `recursive_search()` on its child.
    - If that returns `True`, we know we've found a success case and can return up without any further search.

```python
class Solution:
    """Provided class from LeetCode"""

    def has_path_sum_1(self, root: TreeNode, target_sum: int) -> bool:
        """Tells us if there is a path in the tree that sums to our value.

        Args:
            `root`: A `TreeNode` object that represents the head of the binary tree.
            `target_sum`: The value that we're looking for as a sum
        Returns:
            `bool`: True, if we found a path that sums to the total of `target_sum`
        """

        # Handle empty case
        if root is None:
            return False

        # Is able to look at this value within any level of recursion
        self.target_sum = target_sum

        # Start the search
        return self.recursive_search(root, 0)

    def recursive_search(self, node: TreeNode, cur_total: int) -> bool:
        """Looks through binary tree for a path that has our desired sum.

        Args:
            `node`: The TreeNode object that we're currently looking at.
            `cur_total`: The current total sum, before considering this node. Quickly changes to include this `node`.
        Returns:
            `bool`: True, if we found a path that sums to the total of `target_sum`
        Requirement:
            This function requires a value outside of function scope `target_sum` that each recursive level can see.
        """
        cur_total += node.val

        # If leaf, check to see if the sum is our desired sum
        if node.left is None and node.right is None:
            if cur_total == self.target_sum:
                return True
            else:
                return False
        # If not-leaf, has children.
        # If any child has returned True, we can stop searching.
        else:
            if node.left is not None:
                if self.recursive_search(node.left, cur_total):
                    return True
            if node.right is not None:
                if self.recursive_search(node.right, cur_total):
                    return True
            return False
```

## Tests

### Unit Testing

We implemented unit-tests for this problem with `import unittest`. We designed them for code-coverage, testing edge-cases, and confidence in robustness. We checked for:

- Target not being found within any path
- One node at bottom depth
- Full tree
- Multiple paths with success condition
- Only left children
- Only right children
- Negative sum for total
- No nodes in tree
- Single node in tree
- Two nodes in tree
- All values being zero

We also wrote a separate method `list_to_binary_tree()` in `list_to_binary_tree.py` to generate the binary-tree as connected nodes to hand to our function during testing.

```python
def list_to_binary_tree(our_list, node=None, index=0) -> TreeNode:
    """
    Takes a list representation of a binary tree and returns a node-connected version for traversal.

    Args:
        `list`: A list of integers that represents a given binary tree.
        `index`: The int index in the list of the current node looked-at while in traversal for creation.
    Returns:
        `node`: A TreeNode object that is the head of a created binary tree.
    """

    # Only calls this for the head initial creation.
    # node = None
    if index == 0:
        node = TreeNode(our_list[index], None, None)

    # Creates nodes when we know that we have valid children.
    # Then we step into that child as a new parent.
    new_left_index = index * 2 + 1
    new_right_index = index * 2 + 2
    if new_left_index < len(our_list) and our_list[new_left_index] is not None:
        node.left = TreeNode(our_list[new_left_index], None, None)
        list_to_binary_tree(our_list, node.left, new_left_index)
    if new_right_index < len(our_list) and our_list[new_right_index] is not None:
        node.right = TreeNode(our_list[new_right_index], None, None)
        list_to_binary_tree(our_list, node.right, new_right_index)

    # Only returns the head node.
    return node
```

### Code Coverage

We received 100% code coverage on each tested method from the unit-test using the `coverage.py` tool.

```PowerShell
> coverage run unit_test.py
> coverage html
> coverage report -m 
Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
list_to_binary_tree.py      13      0   100%
path_sum.py                 20      0   100%
path_sum_2.py               18      0   100%
path_sum_3.py               12      0   100%
test_cases.py               47      0   100%
tree_node.py                 5      0   100%
unit_test.py                57      0   100%
------------------------------------------------------
TOTAL                      172      0   100%
```

### Memory Usage Testing

I used `tracemalloc` to look at peak memory block usage during the running of my solution `has_path_sum_1()` and two other people's solutions `has_path_sum_2()` and `has_path_sum_3()`. This is tested on a full binary tree of depth 4, with two correct-solution paths `test_3`.

My solution used 58% the memory of the largest-consuming method.

Memory blocks used:

- `has_path_sum_1()`: 320 blocks
- `has_path_sum_2()`: 320 blocks
- `has_path_sum_3()`: 552 blocks

### Process Time Testing

I used `timeit` to isolate the individual functions on the same test case.

My solution found the result in 75% the time of the slowest method.

- `has_path_sum_1()`: 6.292 x 10^-7 sec
- `has_path_sum_2()`: 8.318 x 10^-7 sec
- `has_path_sum_3()`: 7.084 x 10^-7 sec

## Reflections



## Solution Variations

`has_path_sum_2()` initialized an `isValid` on the object to keep track of if the recursion has found a solution. If it has found one, this becomes `True` and then any next recursion stops itself and returns upward.

Their `if root is None: return 0` is similar to mine, but this is called on every recursion, whereas mine is only called once.

Their mix of `return 0` and `return False` feels like a bad decision. Their ending `return 1 if self.isValid else 0` could be written as `return self.isValid`.

They chose to pass the `total` that we're looking for by arguments into the recursion. They could've done something similar to their `self.isValid`, as I did. I've heard that it's preferred to pass variables in, to avoid outer-scope interactions that may confuse debugging. I'm not sure on a memory-usage difference. If the argument is passed-by-reference, it would use the same amount of memory. In Python, mutable objects--e.g. lists and objects--are passed-by-reference in arguments, but not integers.

```python
# has_path_sum_2()
class Solution:
    def __init__(self):
        self.isValid = False
    def findPathSum(self, root, total, curr_sum):
        if root is None:
            return 0
        if self.isValid == True:
            return self.isValid
        curr_sum += root.val
        if root.left == None and root.right == None:
            if curr_sum == total:
                self.isValid = True
        else:
            self.findPathSum(root.left, total, curr_sum)
            self.findPathSum(root.right, total, curr_sum)
    def has_path_sum_2(self, root: TreeNode, targetSum: int) -> bool:
        self.findPathSum(root, targetSum, 0)
        return 1 if self.isValid else 0
```

`has_path_sum_3` is clean and structured, though it's a hard read with so much on every line and variables with less labeling. Oh, no, this is almost identical to mine, but tightened up.

This person also opted to check `if node:` "if the node is None" every start of recursion, instead of just once at the beginning. The only problem is that it's redundant.

```python
# has_path_sum_3()
class Solution:
    def has_path_sum_3(self, root: TreeNode, targetSum: int) -> bool:
        def go(node, acc):
            if node: 
                if not node.left and not node.right:
                    if acc + node.val == targetSum:
                        return True
                    else:
                        return False
                else:
                    return go(node.left, acc + node.val) or go(
                        node.right, acc + node.val
                    )
            else:
                return False
        return go(root, 0)
```
