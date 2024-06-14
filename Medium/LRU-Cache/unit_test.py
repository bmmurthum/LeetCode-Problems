"""Module for performing unit-tests on my functions"""

import unittest
from lru_cache import LRUCache
from lru_cache_2 import LRUCache as LRUCache_2
from test_cases import TestCases

# pylint: disable=W0622


class Testing(unittest.TestCase):  # pylint: disable=E1101
    """
    Testing class for unittest library
    """

    def __init__(self, method_name: str = "runTest") -> None:
        super().__init__(method_name)
        self.method_count = 2

    def which_method_to_test(self, which, capacity) -> LRUCache:
        """Decide which variation method to test"""
        if which == 1:
            return LRUCache(capacity)
        elif which == 2:
            return LRUCache_2(capacity)

    def test_retrieved_value_within_hash_linked_list(self):
        """Testing value being deeper within the hash-table lists"""
        for w in range(1, self.method_count + 1):
            c = self.which_method_to_test(w, TestCases.act_vals_2[0][0])
            result_list = [None]
            for i, action in enumerate(TestCases.act_list_2):
                if action == "put":
                    c.put(TestCases.act_vals_2[i][0], TestCases.act_vals_2[i][1])
                    result_list.append(None)
                elif action == "get":
                    result_list.append(c.get(TestCases.act_vals_2[i][0]))
            self.assertEqual(
                result_list,
                TestCases.solution_2,
                "The result is incorrect on value deeper within the hash-table lists case.",
            )

    def test_update_on_only_item(self):
        """Testing on update on only single item in hash-table"""
        for w in range(1, self.method_count + 1):
            c = self.which_method_to_test(w, TestCases.act_vals_3[0][0])
            result_list = [None]
            for i, action in enumerate(TestCases.act_list_3):
                if action == "put":
                    c.put(TestCases.act_vals_3[i][0], TestCases.act_vals_3[i][1])
                    result_list.append(None)
                elif action == "get":
                    result_list.append(c.get(TestCases.act_vals_3[i][0]))
            self.assertEqual(
                result_list,
                TestCases.solution_3,
                "The result is incorrect on update on only single item in hash-table case.",
            )

    def test_large(self):
        """Testing large case"""
        for w in range(1, self.method_count + 1):
            c = self.which_method_to_test(w, TestCases.act_vals_1[0][0])
            result_list = [None]
            for i, action in enumerate(TestCases.act_list_1):
                if action == "put":
                    c.put(TestCases.act_vals_1[i][0], TestCases.act_vals_1[i][1])
                    result_list.append(None)
                elif action == "get":
                    result_list.append(c.get(TestCases.act_vals_1[i][0]))
            self.assertEqual(
                result_list,
                TestCases.solution_1,
                "The result is incorrect on larger case.",
            )


if __name__ == "__main__":
    unittest.main()
