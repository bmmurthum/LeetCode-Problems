from collections import deque

class Solution:
    def simplifyPath(self, path: str) -> str:
        # Clean multiples of slashes
        while path != path.replace("//","/"):
            path = path.replace("//","/")
        # Handle edge cases near root
        if path == "/../" or path == "/.." or path == "/" \
            or path == "/." or path == "/./":
            return "/"
        # Remove first and last slashes if exist
        if path[0] == "/":
            path = path[1:]
        if path[-1] == "/":
            path = path[:-1]
        # Prepare for iteration with stack
        chunks = path.split("/")
        stack = deque()
        stackEndPt = 0
        for item in chunks:
            print(item)
        for c in chunks:
            if c == "..":
                if stackEndPt == 0:
                    continue
                else:
                    stack.pop()
                    stackEndPt -= 1
                    continue
            if c == ".":
                continue
            stack.append(c)
            stackEndPt += 1
        # Build new string
        if len(stack) > 0:
            newPath = "/".join(stack)
        else:
            return "/"
        # Add slashes to beginning and end if necessary
        if newPath[0] != "/":
            newPath = "/" + newPath
        if newPath[-1] == "/":
            newPath = newPath[:-1]
        return newPath