"""Problem from LeetCode.com"""

# pylint: disable=C0200


class TrieNode:
    """A Prefix Tree Node"""

    def __init__(self):
        self.child = [None] * 26
        self.word_end = False


class Trie:
    """Class from LeetCode.com"""

    def __init__(self):
        """Initialized the object."""
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Inserts a word into this prefix tree."""

        # Create a node for each letter that has not been seen before.
        # Traverse into the node for the current letter.
        # At the last letter, note this node as a word end.

        node = self.root
        for i in range(len(word)):
            char_val = ord(word[i]) - ord("a")
            if node.child[char_val] is None:
                node.child[char_val] = TrieNode()
            node = node.child[char_val]
        node.word_end = True

    def search(self, word: str) -> bool:
        """
        Looks for this word.

        Args:
            `word`: The search word.
        Returns:
            `True/False`: Whether it's inside the tree.
        """

        # For each letter traverse to the node for that letter.
        # If at any point that node doesn't exist, it must not be stored.
        # At the last node, if this is noted as a word end, return True.

        node = self.root
        for i in range(len(word)):
            char_val = ord(word[i]) - ord("a")
            if node.child[char_val] is None:
                return False
            else:
                node = node.child[char_val]
        if node.word_end is True:
            return True
        return False

    def starts_with(self, prefix: str) -> bool:
        """
        Tells us if theres an inserted word that has the prefix.

        Args:
            `prefix`: The searched prefix.
        Returns:
            `True/False`: Whether there's a word with this prefix.
        """

        # For each letter traverse to the node for that letter.
        # If at any point that node doesn't exist, it must not be stored.

        node = self.root
        for i in range(len(prefix)):
            char_val = ord(prefix[i]) - ord("a")
            if node.child[char_val] is None:
                return False
            else:
                node = node.child[char_val]
        return True
