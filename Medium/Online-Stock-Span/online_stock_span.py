"""Problem from LeetCode.com"""


class StockSpanner:
    """Implement this class from LeetCode.com"""

    def __init__(self):
        self.stack = []
        self.day = 0

    def next(self, price: int) -> int:
        """
        For a given stock price today, this tells us how many days back that
        this value is greater or equal to each of those prices.

        Args:
            `prices`: Today's current price.
        Returns:
            `output`: Days back this value is greater/equal to values.
        """

        # If first value.
        output = 1
        if len(self.stack) == 0:
            self.stack.append([price, self.day])
        else:
            # If value is the lower than recently seen, add to top of stack.
            if price < self.stack[-1][0]:
                self.stack.append([price, self.day])
            # If this is higher than recently seen, handle the stack.
            else:
                earliest_day = None
                while len(self.stack) > 0 and price >= self.stack[-1][0]:
                    earliest_day = self.stack[-1][1]
                    self.stack.pop()
                self.stack.append([price, earliest_day])
                output = 1 + self.day - earliest_day
        self.day += 1
        return output
