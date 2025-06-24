from collections import defaultdict

# Accepted
# Runtime 143 ms Beats 22.48%
# Memory 21.90 MB Beats 82.79%


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        cols = [[row[i] for row in grid] for i in range(len(grid))]

        cnt_repeated = 0

        for row in grid:
            for col in cols:
                if row == col:
                    cnt_repeated += 1

        return cnt_repeated


# Accepted
# Runtime 8 ms Beats 95.23%
# Memory 22.04 MB Beats 35.58%


class Solution_hash:
    def equalPairs(self, grid: list[list[int]]) -> int:
        hashmap = defaultdict(int)
        cols = [[row[i] for row in grid] for i in range(len(grid))]

        for row in grid:
            hashmap[tuple(row)] += 1

        cnt = 0

        for col in cols:
            cnt += hashmap[tuple(col)]

        return cnt


print(Solution().equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))
print(Solution().equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))
print(Solution_hash().equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))
print(
    Solution_hash().equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]])
)
