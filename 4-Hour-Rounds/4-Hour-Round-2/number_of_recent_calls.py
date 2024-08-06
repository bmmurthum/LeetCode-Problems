"""Problem from LeetCode.com"""

from collections import deque


class RecentCounter:
    """Class from LeetCode.com"""

    def __init__(self):
        self.requests = deque()
        self.quantity = 0

    def ping(self, t: int) -> int:
        """
        Pings the queue and returns how many recent pings.

        Args:
            `t`: The current time in milliseconds.
        Returns:
            `self.quantity`: The number of recent pings.
        """
        # Remove time elements that more than 3 seconds old
        while self.quantity != 0:
            if t - self.requests[0] > 3000:
                self.requests.popleft()
                self.quantity -= 1
            else:
                break
        # Add current time
        self.requests.append(t)
        self.quantity += 1
        # Returns the number of recent pings
        return self.quantity
