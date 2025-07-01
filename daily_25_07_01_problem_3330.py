# Accepted
# Runtime 34 ms Beats 84.23%
# Memory 17.67 MB Beats 72.11%


class Solution:
    def possibleStringCount(self, word: str) -> int:
        cnt = 1

        for i in range(len(word) - 1):
            if word[i] == word[i + 1]:
                cnt += 1

        return cnt


print(Solution().possibleStringCount("abbcccc"))
print(Solution().possibleStringCount("abcd"))
print(Solution().possibleStringCount("aaaa"))
print(Solution().possibleStringCount("ere"))
