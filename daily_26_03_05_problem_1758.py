# Accepted
# Runtime 7 ms Beats 83.47%
# Memory 19.16 MB Beats 93.82%

class Solution:
    def minOperations(self, s: str) -> int:
        even_zero = 0
        odd_zero = 0

        for i, digit in enumerate(s):
            if i % 2 == 0:
                if digit == "1":
                    even_zero += 1
                else:
                    odd_zero += 1
            else:
                if digit == "1":
                    odd_zero += 1
                else:
                    even_zero += 1
        return min(even_zero, odd_zero)


print(Solution().minOperations("0100"))
print(Solution().minOperations("10"))
print(Solution().minOperations("10010100"))
print(Solution().minOperations("11001000"))
