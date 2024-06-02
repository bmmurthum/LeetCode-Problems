# Simplify Path

**Description:**

Given an absolute path for a Unix-style file system, which begins with a slash `'/'`, transform this path into its simplified canonical path.

In Unix-style file system context, a single period `'.'` signifies the current directory, a double period `".."` denotes moving up one directory level, and multiple slashes such as `"//"` are interpreted as a single slash. In this problem, treat sequences of periods not covered by the previous rules (like `"..."`) as valid names for files or directories.

The simplified canonical path should adhere to the following rules:

It must start with a single slash `'/'`.
Directories within the path should be separated by only one slash `'/'`.
It should not end with a slash `'/'`, unless it's the root directory.
It should exclude any single or double periods used to denote current or parent directories.
Return the new path.

**Example:**
```
Input: path = "/home/"
Output: "\home"

Input: path = "/home//foo/"
Output: "/home/foo"

Input: path = "/home/user/Documents/../Pictures"
Output: "/home/user/Pictures"

Input: path = "/../"
Output: "/"

Input: path = "/.../a/../b/c/../d/./"
Output: "/.../b/d"
```


## Overview

My solution first cleans the given path-string by removing multiples of neighboring slashes. Then handles the quick assortment of near-root cases `/../` `/..` `/.`. Then we remove prepare the string for `.split("/")` by removing the first and last slashes.

Using the resulting list of names of directories or `/../` and `/./` we iterate through this while handling a stack. We `pop()` from the stack with `/../`, skip over `/./` and `append()` on anything else.

At the end, we rebuild a string from the lasting stack.

We implemented [unit-tests](https://github.com/bmmurthum/LeetCode-Problems/blob/master/Medium/Simplify-Path/test.py) for this problem with `import unittest`. Tests were made for:
- Double slashes `//`
- End slashes `/home/foo/` => `/home/foo`
- Appropriately handling `/../` when mixed in
- Exclusively `/../`
- Three dots `/.../` being valid
- Multiple `/../` in a row, mixed in
- Multiple `/../` towards root, resulting in root
- Multiple slashes `/home//////user`

## Reflections

The given constraints and description didn't lead me to think they'd throw so many curveballs on test cases. I'm surprised Linux would allow `/.../` as a valid directory name or multiple slashes `////` in the path. 