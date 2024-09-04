"""Problem from LeetCode.com"""

# pylint: disable=C0200


class Solution:
    """Problem from LeetCode.com"""

    def find_circle_num(self, is_connected: list[list[int]]) -> int:
        """
        Looking at a matrix that holds information of connected cities, count
        how many "provinces," or cycles.

        Args:
            `is_connected`: A list of each city's connections.
        Returns:
            `province_count`: Number of groups of cities.
        """

        # Start at each city to find how many any one touches.
        # We keep track of "visited" cities to not perform circle calc twice.
        has_been_visited = set()
        province_count = 0
        for i in range(len(is_connected)):

            # Build an initial set of cities to visit from a given start.
            if i not in has_been_visited:
                city = is_connected[i]
                temp_visited = set()
                to_visit = set()
                temp_visited.add(i)
                has_been_visited.add(i)
                for j in range(len(is_connected)):
                    if city[j] == 1 and j not in temp_visited:
                        to_visit.add(j)

                # While still have some to visit, keep looking.
                # Visit the connected towns.
                while len(to_visit) != 0:
                    new_to_visit = set()
                    for city_id in to_visit:
                        if city_id not in temp_visited:
                            temp_visited.add(city_id)
                            has_been_visited.add(city_id)
                            for k in range(len(is_connected)):
                                if (
                                    is_connected[city_id][k] == 1
                                    and k not in temp_visited
                                ):
                                    new_to_visit.add(k)
                    to_visit = new_to_visit

                # Add to province count.
                province_count += 1
        return province_count
