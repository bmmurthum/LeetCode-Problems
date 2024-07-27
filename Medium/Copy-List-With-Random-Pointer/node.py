"""A node definition with a next and a random pointer that points to None, 
   or another node in the list."""


class Node:
    """A node definition with a next and a random pointer that points to None,
    or another node in the list."""

    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random
