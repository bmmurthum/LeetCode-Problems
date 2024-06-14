""" Module to report peak-memory used by method """

import tracemalloc

from lru_cache import LRUCache
from lru_cache_2 import LRUCache as LRUCache_2
from test_cases import TestCases

# pylint: disable=W0622

# Testing Memory Allocation


def run_memory_tests():
    """Runs the collection of memory tests"""

    # My solution
    tracemalloc.start()
    c = LRUCache(TestCases.act_vals_1[0][0])
    for i, action in enumerate(TestCases.act_list_1):
        if action == "put":
            c.put(TestCases.act_vals_1[i][0], TestCases.act_vals_1[i][1])
        elif action == "get":
            c.get(TestCases.act_vals_1[i][0])
    TRACED_MEMORY_PEAK = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("LRUCache Running: " + TRACED_MEMORY_PEAK + " blocks")

    # Someone else's solution
    tracemalloc.start()
    c = LRUCache_2(TestCases.act_vals_1[0][0])
    for i, action in enumerate(TestCases.act_list_1):
        if action == "put":
            c.put(TestCases.act_vals_1[i][0], TestCases.act_vals_1[i][1])
        elif action == "get":
            c.get(TestCases.act_vals_1[i][0])
    TRACED_MEMORY_PEAK = str(tracemalloc.get_traced_memory()[1])
    tracemalloc.stop()
    print("LRUCache_2 Running: " + TRACED_MEMORY_PEAK + " blocks")


run_memory_tests()
