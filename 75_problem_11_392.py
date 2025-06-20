# Accepted
# Runtime 0 ms Beats 100.00%
# Memory 17.94 MB Beats 24.11%


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n_s = len(s)
        if n_s == 0:
            return True
        i_s = 0

        for letter in t:
            if letter == s[i_s]:
                i_s += 1
                if i_s == n_s:
                    return True
        return False


print(Solution().isSubsequence("abc", "ahbgdc"))
print(Solution().isSubsequence("axc", "ahbgdc"))
