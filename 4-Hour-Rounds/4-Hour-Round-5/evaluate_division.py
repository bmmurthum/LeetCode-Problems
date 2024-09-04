"""Problem from LeetCode.com"""

# pylint: disable=C0200


class Solution:
    """Problem from LeetCode.com"""

    def calc_equation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        """
        Given a list of divisions between variables and their results, create a
        list of results of new solutions of divisions between a list of given
        variables. If a variable is unknown, return -1.0 for that "query".

        Args:
            `equations`: A list of given divisions with known outputs.
            `values`: The outputs.
            `queries`: A list of divisions to find results for.
        Returns:
            `output`: An output of results from the queries if possible.
        """

        # Each variable string is a unique value. We'll build a dictionary that
        # serves at a adjacency map for when we compare two equations.

        # adjacency_dict = {
        #     "a": [["a", "b", 2.0]],
        #     "b": [["a", "b", 2.0], ["b", "c", 3.0]],
        #     "c": [["b", "c", 3.0]],
        # }

        # We'll also keep a note on which variables are defined.

        # defined_variables = {"a","b","c"}

        adjacency_dict = {}
        defined_variables = set()
        for i in range(len(equations)):
            item = equations[i]
            if item[0] not in adjacency_dict:
                adjacency_dict[item[0]] = []
            if item[1] not in adjacency_dict:
                adjacency_dict[item[1]] = []
            adjacency_dict[item[0]].append([item[0], item[1], values[i]])
            adjacency_dict[item[1]].append([item[0], item[1], values[i]])
            defined_variables.add(item[0])
            defined_variables.add(item[1])

        # For each query we have three different solution methods.
        # - One of the variables is not known.
        # - Both variables have a defined relation.
        # - There is a path between two variables.

        # We'll build an output list as we iterate through the queries.

        output = []
        for query in queries:

            # If either variable in the query has not been seen, return -1.0.
            if query[0] not in defined_variables or query[1] not in defined_variables:
                output.append(-1.0)
                continue

            # If both variables are equal and known.
            if query[0] == query[1] and query[0] in defined_variables:
                output.append(1.0)
                continue

            # Find immediate solution or inverse.
            found = False
            key = query[0]
            for item in adjacency_dict[key]:
                if query[0] == item[0] and query[1] == item[1]:
                    output.append(item[2])
                    found = True
                    break
                if query[1] == item[0] and query[0] == item[1]:
                    output.append(1 / item[2])
                    found = True
                    break
            if found is True:
                continue

            # Do a breadth-first search for a path between the two unshared
            # variables. Keeping a math note as we go.

            # Building starting points.
            to_process = list()
            visited = set()
            key = query[0]
            visited.add(query[0])
            for item in adjacency_dict[key]:
                if item[0] == key and item[1] not in visited:
                    to_process.append(item)
                    continue
                if item[1] == key and item[0] not in visited:
                    flipped_item = [item[1], item[0], 1 / item[2]]
                    to_process.append(flipped_item)
                    continue

            found_solution = False
            while len(to_process) > 0 and not found_solution:
                temp = list()
                for item in to_process:
                    # Check for solution.
                    if query[0] in item and query[1] in item:
                        found_solution = True
                        if query[0] == item[0]:
                            output.append(item[2])
                        else:
                            output.append(1 / item[2])
                        break
                    # Iterate the breadth search.
                    if item[0] not in visited:
                        key = item[0]
                        for new_item in adjacency_dict[key]:
                            if new_item[0] == key and new_item[1] not in visited:
                                result = self.handle_merge(item, new_item)
                                temp.append(result)
                                continue
                            if new_item[1] == key and new_item[0] not in visited:
                                result = self.handle_merge(item, new_item)
                                temp.append(result)
                                continue
                        visited.add(key)
                    if item[1] not in visited:
                        key = item[1]
                        for new_item in adjacency_dict[key]:
                            if new_item[0] == key and new_item[1] not in visited:
                                result = self.handle_merge(item, new_item)
                                temp.append(result)
                                continue
                            if new_item[1] == key and new_item[0] not in visited:
                                result = self.handle_merge(item, new_item)
                                temp.append(result)
                                continue
                        visited.add(key)
                to_process = temp
            if found_solution is False:
                output.append(-1.0)
        return output

    def handle_merge(
        self, a: list[str, str, float], b: list[str, str, float]
    ) -> list[str, str, float]:
        """
        Given two divisions, return a new one without the shared variable.

        Requires that our interested variable is on the left inside the first
        input "a". This returns a new division with that interested variable
        still in the same spot.

        Case 1
        a = [x5, x4, 6.0]
        b = [x4, x3, 5.0]
        output = [x5, x3, 30.0]

        Case 2
        a = [x5, x4, 6.0]
        b = [x3, x4, 3.0]
        output = [x5, x3, 2.0]

        Args:
            `a`: Some division between two variables.
            `b`: Some division between two variables.
        Returns:
            `output`: Some new division between two variables.
        """

        shared_var = a[1]
        if b[1] == shared_var:
            result = a[2] / b[2]
            return [a[0], b[0], result]
        if b[0] == shared_var:
            result = a[2] * b[2]
            return [a[0], b[1], result]
