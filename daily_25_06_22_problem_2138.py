# Accepted
# Runtime 0 ms Beats 100.00%
# Memory 17.58 MB Beats 98.64%


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        ans = []
        for i in range(0, len(s), k):
            group = s[i : i + k]
            n_group = len(group)
            if n_group == k:
                ans.append(group)
            else:
                ans.append(group + (fill * (k - n_group)))
        return ans


print(Solution().divideString("abcdefghi", 3, "x"))
print(Solution().divideString("abcdefghij", 3, "x"))
