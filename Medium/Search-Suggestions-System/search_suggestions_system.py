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

    def three_matches(self, prefix: str) -> list:
        """
        Returns at most three matches to the prefix search. If more than three,
        return the first three in alphabetical order.

        Args:
            `prefix`: The interested string.
        Returns:
            `output`: The list of found strings.
        """

        def recursive_help(
            prefix: str, node: TrieNode, suffix: list, output: list
        ) -> None:
            """
            Traverses the tree building `output` with a list of found words in
            alphabetical order.

            Because `output` is mutable, it's passed by reference and editing
            it with push() pop() will be carried out without returning it.

            prefix = "app"
            suffix = ["l","e"]
            output = ["app","apple"]

            Args:
                `prefix`: The initial search.
                `node`: The current node we're at.
                `suffix`: The built list of newer characters to look at.
                `output`: The generated list of words.
            """

            # Handle word ending mid-branch.
            if node.word_end is True:
                temp = "".join(suffix)
                temp = prefix + temp
                output.append(temp)

            if len(output) > 2:
                return

            # Search into another branch.
            for i in range(26):
                branch = node.child[i]
                if branch is not None:
                    char = chr(i + ord("a"))
                    suffix.append(char)
                    recursive_help(prefix, branch, suffix, output)
                    suffix.pop()
                if len(output) > 2:
                    return

        # Iterate through the tree with a left-traversal, adding word as we
        # reach them, both within the tree and at the leaves.

        # Start the traversal at the last letter of the prefix, adding the
        # prefix, if it itself is a word.

        output = []

        # Traverse to the end of the prefix.
        node = self.root
        for i in range(len(prefix)):
            char_val = ord(prefix[i]) - ord("a")
            # If we can't reach the entire prefix, there are no words.
            if node.child[char_val] is None:
                return []
            else:
                node = node.child[char_val]

        # If the the prefix has been added as a word.
        if node.word_end is True:
            output.append(prefix)

        # Perform the recursive search
        suffix = []
        for i in range(26):
            branch = node.child[i]
            if branch is not None:
                char = chr(i + ord("a"))
                suffix.append(char)
                recursive_help(prefix, branch, suffix, output)
                suffix.pop()
            if len(output) > 2:
                break

        return output


class Solution:
    """Problem from LeetCode.com"""

    def suggested_products(
        self, products: list[str], search_word: str
    ) -> list[list[str]]:
        """
        Given a list of words that are in our system `products`, for each
        character added to a typed `search_word` return three suggestions that
        match these as a prefix.

        These outputs should be added to a list to then be returned.

        Args:
            `products`: The entries into the system.
            `search_word`: The full search word.
        Returns:
            `output`: The compiled list of outputs.
        """

        # Add all the products to the system.
        system = Trie()
        for item in products:
            system.insert(item)

        # Call on our recursive Trie function.
        output = []
        word = ""
        for letter in search_word:
            word = word + letter
            output.append(system.three_matches(word))
        return output
