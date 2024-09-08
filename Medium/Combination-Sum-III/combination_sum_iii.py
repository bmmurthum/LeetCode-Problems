"""Problem from LeetCode.com"""

# pylint: disable=E4703


class Solution:
    """Problem from LeetCode.com"""

    def combination_sum_3(self, k: int, n: int) -> list[list[int]]:
        """
        Finds a combination of `k` number of integers that sum to `n`. These
        numbers are between 1-9 inclusive. We're guaranteed 2 <= k <= 9.

        Args:
            `k`: An amount of numbers to add to the sum.
            `n`: The target sum.
        Returns:
            `output`: A list of lists of values that sum to the target.
        """

        def backtracking(built: list, current_depth: int, this_total: int) -> None:
            """
            Start a recursive search that builds a current-numbers-looked-at
            `built` list that may sum to our target. We keep track of the total
            of these numbers in `this_total` to avoid calling sum() many times.
            We stop recursion at the target depth of `k`.

            We're minimizing our `values` list over time.

            Args:
                `built`: The current numbers considered for a possible sum.
                `current_depth`: The current depth in recursion.
                `this_total`: The current sum of the `built` list.
            """

            # Start a branch for each value available to us. Stop early if
            # possible. Remove possibilities as going deeper. Remove
            # possibilities after knowing its been covered.
            for item in values:
                if item < built[-1]:
                    continue

                current_total = this_total + item
                # If still possible to be found.
                if current_total < n:

                    # If at end-depth
                    if current_depth + 1 == k:
                        if (n - current_total) > item and (n - current_total) in values:
                            built.append(item)
                            built.append(n - current_total)
                            output.append(built.copy())
                            built.remove(item)
                            built.remove(n - current_total)
                        elif (n - current_total) < item:
                            break
                    # If can do deeper, go deeper.
                    else:
                        values.remove(item)
                        built.append(item)
                        backtracking(built, current_depth + 1, current_total)
                        values.add(item)
                        built.remove(item)
                # Not possible in this path, stop depth search from this branch.
                else:
                    break

        values = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        output = []

        # Edge-case: The target is below a possible minimum.
        val_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        bottom_k_sum = sum(val_list[:k])
        top_k_sum = sum(val_list[-k:])
        if n < bottom_k_sum:
            return []
        # Edge-case: The target is above a possible maximum.
        if n > top_k_sum:
            return []
        # Edge-case: The target is equal to the top-or-bottom sums.
        if n == bottom_k_sum:
            return [val_list[:k]]
        if n == top_k_sum:
            return [val_list[-k:]]
        # Edge-case: k == 2. My backtracking requires k > 2.
        if k == 2:
            for val in val_list:
                if n - val in values and (n - val) > val:
                    output.append([val, n - val])
            return output

        # Start the backtracking recursion.
        for val in val_list:
            values.remove(val)
            backtracking([val], 2, val)

        return output
