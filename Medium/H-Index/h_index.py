""" Module to return the value of the element that is a majority of the items in a list. """

# Comment lines too long. We want to adhere to Google's spec on docstrings.
# pylint: disable=C0301
# Attribute defined outside of method. Helps clarity to allow this.
# pylint: disable=W0201


class Solution:
    """Problem given by LeetCode."""

    def h_index(self, citations: list[int]) -> int:
        """
        Return the H-Index value of a group of an author's papers, given each
        item in the list is a paper's number of citations.

        https://en.wikipedia.org/wiki/H-index

        Args:
            `citations`: A list of number of citations that each published
                paper by this author has.
        Returns:
            `h_index`: The value.
        """
        citations.sort(reverse=True)
        for i, val in enumerate(citations):
            if i >= val:
                return i
        return len(citations)
