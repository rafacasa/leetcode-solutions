# Accepted
# Runtime 0 ms Beats 100.00%
# Memory 17.74 MB Beats 81.16%


class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        ans = 0
        while k != 1:
            exp_2 = k.bit_length() - 1

            if (1 << exp_2) == k:
                exp_2 -= 1

            first_half_size = 1 << exp_2
            k -= first_half_size

            if operations[exp_2]:
                ans += 1

        return chr(ord("a") + (ans % 26))
