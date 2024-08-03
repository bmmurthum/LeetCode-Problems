""" This module to call all collections of tests on this problem. """

# cSpell:disable

from memory_tests import MemoryTests
from time_tests import TimeTests
from unit_tests import UnitTests


class CallAllTests:
    """Calls all tests."""

    def call(self):
        """Calls the tests."""

        UnitTests().run_unit_tests()
        print("")
        MemoryTests().run_memory_tests()
        print("")
        TimeTests().run_time_tests()
        print("")


if __name__ == "__main__":
    CallAllTests().call()
