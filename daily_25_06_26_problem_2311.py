# Accepted
# Runtime 4 ms Beats 51.22%
# Memory 17.96 MB Beats 31.71%


class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        dec_s = 0
        i = len(s) - 1
        cnt_digits = None
        while i >= 0:
            dec_s = int(s[i:], base=2)
            if dec_s > k:
                cnt_digits = len(s) - i - 1
                break
            i -= 1
        if cnt_digits is None:
            return len(s)

        cnt_zero = len([a for a in s[:i] if a == "0"])
        return cnt_digits + cnt_zero


print(Solution().longestSubsequence(s="1001010", k=5))
print(Solution().longestSubsequence(s="00101001", k=1))
print(Solution().longestSubsequence(s="0", k=1))
print(Solution().longestSubsequence(s="0111101", k=518459120))
