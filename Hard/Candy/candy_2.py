class Solution:
    def candy_2(self, ratings: list[int]) -> int:
        length = len(ratings)
        total, up, down, peak = 1, 0, 0, 1
        for idx in range(1, length):
            prev, curr = ratings[idx - 1], ratings[idx]
            if curr > prev:
                up += 1
                total += 1 + up
                peak, down = 1 + up, 0
            elif curr < prev:
                down += 1
                total += down + int(peak <= down)
                up = 0
            else:
                up, down, peak = 0, 0, 1
                total += 1
        return total
