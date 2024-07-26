class Solution:
    def insert_3(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        n = len(intervals)
        i = 0
        j = n
        while i < j:
            mid = i + (j - i) // 2
            if intervals[mid][0] <= newInterval[0]:
                i = mid + 1
            else:
                j = mid
        if i != 0 and intervals[i - 1][1] >= newInterval[0]:
            ans = intervals[: i - 1]
            ans.append([intervals[i - 1][0], max(intervals[i - 1][1], newInterval[1])])
        else:
            ans = intervals[:i]
            ans.append(newInterval)
        j = n
        while i < j:
            mid = i + (j - i) // 2
            if intervals[mid][1] >= ans[-1][1]:
                j = mid
            else:
                i = mid + 1
        if i != n and intervals[i][0] <= ans[-1][1]:
            ans[-1][1] = max(intervals[i][1], ans[-1][1])
            ans += intervals[i + 1 :]
        else:
            ans += intervals[i:]
        return ans


# if __name__ == "__main__":
#     import json, sys

#     with open("user.out", "w") as f:
#         data = map(json.loads, sys.stdin)
#         testcases = zip(*[iter(data)] * 2, strict=True)
#         for intervals, interval in testcases:
#             result = insert(intervals, interval)
#             print(json.dumps(result, separators=(",", ":")), file=f)
#     sys.exit()
