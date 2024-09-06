"""Problem from LeetCode.com"""

import heapq


class Solution:
    """Problem from LeetCode.com"""

    def total_cost(self, costs: list[int], k: int, candidates: int) -> int:
        """
        Given a list of the costs to hire an employee, `costs`, where
        `costs[i]` is the cost to hire this `i` worker. We're looking to hire
        `k` workers with the minimum money spent.

        For each hiring round, we must choose between workers at the front and
        back of the list `cost` with the width of `candidates`.

                 .   .                    .   .
        costs = [17, 12, 10, 2, 7, 2, 11, 20, 8]
        candidates = 2
        k = 5
        example_1st_round = [17, 12] + [20, 8]
        costs_after = [17, 12, 10, 2, 7, 2, 11, 20]

        Args:
            `costs`: A list of potential employees to hire and their cost.
            `k`: A target number of employees to hire.
            `candidates`: A width of employees in a hiring round.
        Returns:
            `total_cost`: The total cost to hire these employees.
        """

        # Handle edge-case.
        # If the candidates-window reaches across whole list.
        if candidates > (len(costs) // 2):
            heapq.heapify(costs)
            total_cost = 0
            for _ in range(k):
                total_cost += heapq.heappop(costs)
            return total_cost

        # Handle edge-case.
        # If candidates-window is 1, looking at only left and right at any
        # point.
        if candidates == 1:
            left_ptr = 0
            right_ptr = len(costs) - 1
            total_cost = 0
            for _ in range(k):
                if costs[left_ptr] <= costs[right_ptr]:
                    total_cost += costs[left_ptr]
                    left_ptr += 1
                else:
                    total_cost += costs[right_ptr]
                    right_ptr -= 1
            return total_cost

        # Handle edge-case.
        # If we need to hire every worker.
        if k == len(costs):
            return sum(costs)

        # Holding all the potential hires.
        left_heap = costs[:candidates]
        right_heap = costs[-1 * candidates :]
        heapq.heapify(left_heap)
        heapq.heapify(right_heap)

        # A next person-index to add to pool for either side.
        left_ptr = candidates
        right_ptr = len(costs) - candidates - 1

        # Look at the left group and right group for hires, hiring and adding
        # new candidates to the hiring groups accordingly. If the two hiring
        # groups can be combined, we'll break from this loop to loop
        # differently.
        total_cost = 0
        total_hires = 0
        while total_hires < k:
            if left_heap[0] <= right_heap[0]:
                total_cost += heapq.heapreplace(left_heap, costs[left_ptr])
                left_ptr += 1
            else:
                total_cost += heapq.heapreplace(right_heap, costs[right_ptr])
                right_ptr -= 1
            total_hires += 1
            if left_ptr > right_ptr:
                break

        # Once the two heaps cover all that's left, we can merge them and sort
        # and then just consider hiring from the minimum values.
        if left_ptr > right_ptr and total_hires < k:
            new_list = left_heap + right_heap
            new_list.sort()
            i = 0
            while total_hires < k:
                total_cost += new_list[i]
                total_hires += 1
                i += 1

        return total_cost
