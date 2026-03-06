# Accepted
# Runtime 4 ms Beats 88.03%
# Memory 20.78 MB Beats 86.71%

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        maxRight = []
        for line in grid:
            for i in range(n - 1, -1, -1):
                if line[i] == 1:
                    maxRight.append(i)
                    break
                if i == 0:
                    maxRight.append(-1)
        moves = 0
        ok = False
        for n_line in range(n):
            for i_rigth in range(n_line, n):
                if maxRight[i_rigth] <= n_line:
                    moves += i_rigth - n_line
                    maxRight.pop(i_rigth)
                    maxRight.insert(0, i_rigth)
                    ok = True
                    break
            if ok:
                ok = False
            else:
                return -1
        return moves

print(Solution().minSwaps([[0, 0, 1], [1, 1, 0], [1, 0, 0]]))
print(Solution().minSwaps([[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]]))
print(Solution().minSwaps([[1, 0, 0], [1, 1, 0], [1, 1, 1]]))
print(Solution().minSwaps([[0, 0, 1], [0, 0, 0], [0, 0, 0]]))
