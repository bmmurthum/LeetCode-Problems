class Solution:
    def insert_2(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        result = []
        pos = 0
        while pos < len(intervals):
            if intervals[pos][0] > newInterval[1]:
                break
            elif intervals[pos][1] < newInterval[0]:
                result.append(intervals[pos])
            else:
                newInterval = [
                    min(newInterval[0], intervals[pos][0]),
                    max(newInterval[1], intervals[pos][1]),
                ]
            pos += 1
        result.append(newInterval)
        for i in range(pos, len(intervals)):
            result.append(intervals[i])
        return result
