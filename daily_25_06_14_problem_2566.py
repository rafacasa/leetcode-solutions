# Accepted
# Runtime 0 ms Beats 100.00%
# Memory 17.62 MB Beats 76.62%


class Solution:
    def minMaxDifference(self, num: int) -> int:
        max = [s for s in str(num)]
        min = [s for s in str(num)]
        to_nine = None
        to_zero = None
        for i, digit in enumerate(max):
            if not to_nine and digit != "9":
                to_nine = digit
            if not to_zero and digit != "0":
                to_zero = digit
            if digit == to_nine:
                max[i] = "9"
            if digit == to_zero:
                min[i] = "0"

        return int("".join(max)) - int("".join(min))


print(Solution().minMaxDifference(11891))
print(Solution().minMaxDifference(90))
