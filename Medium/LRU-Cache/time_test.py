"""Module for testing function time performance"""

import timeit


NUM_TESTS = 500


# My solution
MYSETUP = """
from lru_cache import LRUCache
from test_cases import TestCases
"""
MYCODE = """
c = LRUCache(TestCases.act_vals_1[0][0])
for i, action in enumerate(TestCases.act_list_1):
    if action == "put":
        c.put(TestCases.act_vals_1[i][0], TestCases.act_vals_1[i][1])
    elif action == "get":
        c.get(TestCases.act_vals_1[i][0])
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("LRUCache Running Time: " + TIME_PER_RUN)


# Someone else's solution
MYSETUP = """
from lru_cache_2 import LRUCache
from test_cases import TestCases
"""
MYCODE = """
c = LRUCache(TestCases.act_vals_1[0][0])
for i, action in enumerate(TestCases.act_list_1):
    if action == "put":
        c.put(TestCases.act_vals_1[i][0], TestCases.act_vals_1[i][1])
    elif action == "get":
        c.get(TestCases.act_vals_1[i][0])
"""
TIME_PER_RUN = str(
    timeit.timeit(setup=MYSETUP, stmt=MYCODE, number=NUM_TESTS) / NUM_TESTS
)
print("LRUCache_2 Running Time: " + TIME_PER_RUN)
