class Solution:
    def h_index_2(self, citations: list[int]) -> int:
        count = [0] * (max(citations) + 1)
        for c in citations:
            count[c] += 1
        paper_count = 0
        for number_cited in range(len(count) - 1, -1, -1):
            paper_count += count[number_cited]
            if paper_count >= number_cited:
                return number_cited
