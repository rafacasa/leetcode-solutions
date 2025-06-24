# Accepted
# Runtime 0 ms Beats 100.00%
# Memory 17.95 MB Beats 9.94%


class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        max_sum = 0
        value = 0

        for i in gain:
            value += i
            max_sum = max(max_sum, value)

        return max_sum


print(Solution().largestAltitude([-5, 1, 5, 0, -7]))
print(Solution().largestAltitude([-4, -3, -2, -1, 4, 3, 2]))
