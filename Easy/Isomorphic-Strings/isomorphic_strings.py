""" Module to tell if two strings are isomorphic to one another. """

# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201


class Solution:
    """Problem given by LeetCode."""

    def is_isomorphic(self, s: str, t: str) -> bool:
        """
        Tells us if two strings are isomorphic to each other.

        Args:
            `s`: One string
            `t`: Another string
        Returns:
            `True/False`: If strings are isomorphic.
        """

        found = {}
        for a, b in zip(s, t):
            # If both have not been seen.
            if a not in found.keys() and b not in found.values():
                found[a] = b
            # This key/value is recorded, but not the other.
            elif (a not in found.keys() and b in found.values()) or (
                a in found.keys() and b not in found.values()
            ):
                return False
            # Current value doesn't match
            elif a in found.keys() and found[a] != b:
                return False
        return True
