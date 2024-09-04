"""Problem from LeetCode.com"""


class Solution:
    """Problem from LeetCode.com"""

    def min_reorder(self, n: int, connections: list[list[int]]) -> int:
        """
        Looking at a list of connections between cities, return a int number of
        changes to the roads to have them all lead to the "capitol" of index-0.

        Args:
            `connections`: A list of each city's connections.
        Returns:
            `change_count`: A number of changed connections.
        """

        # Build a graph for traversing.
        visited = [0 for _ in range(n)]
        adjacency_list = [[] for _ in range(n)]
        for edge in connections:
            adjacency_list[edge[0]].append(edge)
            adjacency_list[edge[1]].append(edge)

        # Starting at the capitol, index 0, do breadth search.
        visited[0] = 1
        to_visit = set()
        reverse_count = 0
        for edge in adjacency_list[0]:
            if edge[0] == 0:
                to_visit.add(edge[1])
                reverse_count += 1
            else:
                to_visit.add(edge[0])

        # Keep looking into connections while we find more. If a connection is
        # in the wrong direction, increase our count.
        while len(to_visit) > 0:
            temp = set()
            for city_index in to_visit:
                for city_connections in adjacency_list[city_index]:
                    if (
                        city_connections[0] == city_index
                        and visited[city_connections[1]] == 0
                    ):
                        reverse_count += 1
                        temp.add(city_connections[1])
                    if (
                        city_connections[1] == city_index
                        and visited[city_connections[0]] == 0
                    ):
                        temp.add(city_connections[0])
                visited[city_index] = 1
            to_visit = temp
        return reverse_count
