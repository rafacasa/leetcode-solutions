from collections import Counter

# Accepted
# Runtime 0 ms Beats 100.00%
# Memory 18.01 MB Beats 9.66%


class Solution:
    def findLucky(self, arr: list[int]) -> int:
        cnt = Counter(arr)

        ans = -1
        for n, c in cnt.items():
            if n == c:
                ans = max(ans, n)

        return ans


print(Solution().findLucky([2, 2, 3, 4]))
print(Solution().findLucky([1, 2, 2, 3, 3, 3]))
print(Solution().findLucky([2, 2, 2, 3, 3]))
