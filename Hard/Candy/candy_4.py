class Solution:
    def candy_4(self, ratings: list[int]) -> int:
        self.ratings = ratings
        self.candies = {}
        for i in range(len(ratings)):
            self.dfs(i)
        return sum(self.candies.values())

    def dfs(self, ind):
        if ind in self.candies:
            return self.candies[ind]
        val = self.ratings[ind]
        left = self.ratings[ind - 1] if ind - 1 >= 0 else val
        right = self.ratings[ind + 1] if ind + 1 < len(self.ratings) else val
        if val > left and val > right:
            left_candy = self.dfs(ind - 1)
            right_candy = self.dfs(ind + 1)
            candy = max(left_candy, right_candy) + 1
        elif val > left:
            candy = self.dfs(ind - 1) + 1
        elif val > right:
            candy = self.dfs(ind + 1) + 1
        else:
            candy = 1
        self.candies[ind] = candy
        return self.candies[ind]
