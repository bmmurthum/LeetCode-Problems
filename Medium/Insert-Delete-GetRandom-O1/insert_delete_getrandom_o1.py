""" Module to find the minimum jumping path to the end index. """

# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201

import random


class RandomizedSet:
    """Class given by LeetCode. Implement."""

    def __init__(self):
        self.held_values = set()

    def insert(self, val: int) -> bool:
        """Inserts an element to the set."""
        if val in self.held_values:
            return False
        else:
            self.held_values.add(val)
            return True

    def remove(self, val: int) -> bool:
        """Removes an element from the set if inside."""
        if val in self.held_values:
            self.held_values.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        """Return a random value from the set."""
        return random.choice(list(self.held_values))
