"""Problem from LeetCode.com"""

# pylint: disable=C0200


class Solution:
    """Problem from LeetCode.com"""

    def min_distance(self, word1: str, word2: str) -> int:
        """
        Find the number of changes that need to made to `word1` such that it
        will now be `word2`. We can add a letter, remove a letter, or change a
        letter.

        Args:
            `word1`: A given string.
            `word2`: A given string.
        Returns:
            `changes`: The number of changes needed.
        """

        # We penciled out some cases to look for a pattern in logic in the
        # output grid. Doing this was enough to see a pattern.

        # Edge-cases: Handle empty strings.
        if word1 == "" and word2 == "":
            return 0
        if word1 == "" and len(word2) > 0:
            return len(word2)
        if word2 == "" and len(word1) > 0:
            return len(word1)

        # Initialize a grid with all zeroes.
        grid = [[0 for _ in range(len(word1))] for _ in range(len(word2))]

        # Have the outer layers custom-handled.
        found = 0
        for i in range(len(grid[0])):
            if word1[i] == word2[0]:
                found = -1
            grid[0][i] = i + found + 1
        found = 0
        for j in range(len(grid)):
            if word2[j] == word1[0]:
                found = -1
            grid[j][0] = j + found + 1

        # Starting at [1,1] generate the board with calculations based on
        # the neighbors to the top, left and top-left and whether this
        # character is matched between the two strings.
        for x in range(1, len(grid[0])):
            for y in range(1, len(grid)):
                if word1[x] == word2[y]:
                    grid[y][x] = grid[y - 1][x - 1]
                else:
                    grid[y][x] = (
                        min([grid[y - 1][x], grid[y][x - 1], grid[y - 1][x - 1]]) + 1
                    )

        # Return the value of the bottom right corner.
        output = grid[len(grid) - 1][len(grid[0]) - 1]
        return output

    def min_distance_2(self, word1: str, word2: str) -> int:
        """
        Find the number of changes that need to made to `word1` such that it
        will now be `word2`. UNFINISHED.

        Args:
            `word1`: A given string.
            `word2`: A given string.
        Returns:
            `changes`: The number of changes needed.
        """

        def longest_common_subsequence(text1: str, text2: str) -> int:
            """
            Find the string of the longest shared subsequence.

            Ex: text1 = "abcde", text2 = "acfe", shared = "ace"

            Args:
                `text1`: A first string.
                `text2`: A second string.
            Returns:
                `output`: The longest shared subsequence.
            """

            # Initialize a grid with all zeroes.
            grid = [[0 for _ in range(len(text1))] for _ in range(len(text2))]
            found = 0
            for i in range(len(grid[0])):
                if text1[i] == text2[0]:
                    found = 1
                grid[0][i] = found
            found = 0
            for j in range(len(grid)):
                if text2[j] == text1[0]:
                    found = 1
                grid[j][0] = found

            # Starting at [1,1] generate the board with calculations based on
            # the neighbors to the top, left and top-left and whether this
            # character is matched between the two strings.
            for x in range(1, len(grid[0])):
                for y in range(1, len(grid)):
                    if text1[x] == text2[y]:
                        grid[y][x] = grid[y - 1][x - 1] + 1
                    else:
                        grid[y][x] = max(grid[y - 1][x], grid[y][x - 1])

            # Rebuild the string from the bottom right grid pattern.
            built = ""
            length = grid[len(grid) - 1][len(grid[0]) - 1]
            i = 0
            x = len(grid[0]) - 1
            y = len(grid) - 1
            while i < length:
                if min(grid[y - 1][x], grid[y][x - 1]) == grid[y][x] - 1:
                    built = text1[x] + built
                    y -= 1
                    i += 1
                x -= 1

            # Return rebuilt shared string.
            return built

        def generate_words_with_substring(
            word: str, substring: str, built: str = "", pos: int = 0, depth: int = 0
        ) -> str:
            """
            Builds a collection of valid positions of the substring within the
            word.

            Ex:
            word == "execution",
            substring = "etion",
            output == ["e____tion","__e__tion"]

            Args:
                `word`: The given longer word.
                `substring`: The given substring within the word.
                `built`: The currently-being-made string.
                `pos`: The current position within `word`.
                `depth`: The current position within `substring.
            Returns:
                `output`: The list of possible placements.
            """

            # If we're not going to be able to find this letter, stop.
            if substring[depth] not in word[pos:]:
                return None
            # Build and branch-off when finding a letter-match.
            output = []
            branch = []
            my_built = built
            for i in range(pos, len(word)):
                if word[i] == substring[depth]:
                    x = generate_words_with_substring(
                        word, substring, my_built + "_", i + 1, depth
                    )
                    if x is not None:
                        for item in x:
                            branch.append(item)
                    my_built = my_built + word[i]
                    depth += 1
                else:
                    my_built += "_"
            # If this created a valid word, add it to a list to return.
            if depth == len(substring):
                output.append(my_built)
            # If any of the branches of recursion created valid words, add those.
            if len(branch) > 0:
                for item in branch:
                    output.append(item)
            # Return upward, our list of generated words.
            if len(output) != 0:
                return output
            else:
                return None

        # This is an unfinished method.

        # The idea was that we'll find the string of the shared largest
        # subsequence. To then find the variations of each word with those
        # letters being the only ones highlighted. We could then use these as
        # items to compare to look for manipulations that would get to the
        # desired output.

        # It uses recursion in generate_words_with_substring() in addition to
        # the dynamic-programming from longest_common_subsequence().

        # The possibility of it being more efficient than my other solution was
        # based in that when we imagine two strings of length 500, the other
        # solution has to do memory accesses for 250,000 writes and some
        # multiple of that as reads for comparisons.

        # Because this method also does a similar DP approach, it's just as
        # slow. Initially I thought the pure DP approach wasn't possible, so I
        # was using an intermediary tool to look for a recursive solution.

        # I'm happy with longest_common_subsequence() as an idea, to use the
        # generated table to reverse through to find the substring.

        # I'm happy with the recursive look for finding those substrings within
        # the initial words. Maybe I'll be able to use them in another problem.

        # Find a longest shared substring.
        longest_common_shared = longest_common_subsequence(word1, word2)

        # Generate the possible words with their substrings highlighted.
        test = generate_words_with_substring(word1, longest_common_shared)
        test2 = generate_words_with_substring(word2, longest_common_shared)

        # TODO - This is unusable.
        return -1
