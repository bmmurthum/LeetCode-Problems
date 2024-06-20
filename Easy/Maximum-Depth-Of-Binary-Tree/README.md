# Maximum Depth of Binary Tree

**Description:**

Given the `root` of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

**Example:**

```text
Example:

    3
   / \
  9  20
     / \
    15  7

Returns: 3
```

## Overview

For my solution, we implement a simple recursive method to look into each of the given `root` node's children. Within the recursion, `root` represents the currently-looked-at leaf of type `TreeNode`.

If at a bottom, in which a node has no children, this method is called on those `None` children to return 0 to this parent. This bottom leaf sees those 0s and returns the maximum between them and adds itself to a current total.

When a leaf has any amount of children, it compares the values its children returned to it and returns the maximum between them and adds itself.

When at the `root`, this totals to the maximum depth of the tree.

```python
def max_depth_1(self, root: TreeNode) -> int:
    """Returns the maximum depth of a binary tree from the `root` node."""

    if root is None:
        return 0
    left_max = self.max_depth_1(root.left)
    right_max = self.max_depth_1(root.right)
    maximum = max(left_max, right_max)
    return maximum + 1
```

## Tests

### Unit Testing

We implemented unit-tests for this problem with `import unittest`. We designed them for code-coverage, testing edge-cases. We checked for:

- Zero nodes in the tree
- One node
- Two nodes depth
- Three nodes depth with a branch

### Code Coverage

We received 100% code coverage on each tested method from the unit-test using the `coverage.py` tool.

```PowerShell
> coverage run unit_test.py
> coverage html
> coverage report -m 
Name                                Stmts   Miss  Cover
-----------------------------------------------------------------
maximum_depth_of_binary_tree.py         9      0   100%
maximum_depth_of_binary_tree_2.py       6      0   100%
test_cases.py                          15      0   100%
tree_node.py                            5      0   100%
unit_test.py                           33      0   100%
-----------------------------------------------------------------
TOTAL                                  68      0   100%
```

### Memory Usage Testing

I used `tracemalloc` to look at peak memory block usage during the running of my solution `max_depth_1` and the same without assigning internal variables `max_depth_2`. This is tested on the case of a simple tree with a maximum depth of 3.

Memory blocks used:

- `max_depth_1()`: 48 blocks
- `max_depth_2()`: 48 blocks

### Process Time Testing

I used `timeit` to isolate the individual functions on the same input. The solution without assignment of variables is 15% faster.

- `max_depth_1()`: 6.818 x 10^-7 sec
- `max_depth_2()`: 5.784 x 10^-7 sec

## Reflections

To see better variation between optimization test and general robustness, in testing I'd like to setup larger test cases. Though, the payoff of time writing to quality of testing doesn't seem valuable here.

In this exercise Pylint threw me warnings that the `TestCase` variables aren't being correctly imported to the `unit_test.py` tests. At first it seemed that it was related to Pylint not recognizing the `import TreeNode` inside of `test_cases.py`, but then seemed to expand to all variables in the test cases. Within Visual Studio, I ran the command `>Pylint Restart Server` and Pylint figured itself out.

Within the `memory_test.py`, we get different memory usage if we call for the `Solution` object within the scope of the test. I left this outside of scope because I'm interested in the used memory within the action of the function to compare our two solutions. In a different moment, I might consider the overall usage of memory to perform all tasks from the initial running of the program.

## Solution Variations

This solution is identical to mine in function, but doesn't call for saving any results to variables for temporary holding.

```python
# Someone else's solution
def max_depth_2(self, root: TreeNode) -> int:
    """Returns the maximum depth of a binary tree from the `root` node."""

    if root is None:
        return 0
    else:
        return max(self.max_depth_2(root.left), self.max_depth_2(root.right)) + 1
```
