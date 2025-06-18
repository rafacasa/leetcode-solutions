# Accepted
# Runtime 41 ms Beats 36.66%
# Memory 17.59 MB Beats 94.42%


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        for i in range(min(len(word1), len(word2))):
            ans.append(word1[i])
            ans.append(word2[i])
        ans.append(word1[i + 1 :])
        ans.append(word2[i + 1 :])

        return "".join(ans)


print(Solution().mergeAlternately("abc", "pqr"))
print(Solution().mergeAlternately("ab", "pqrs"))
print(Solution().mergeAlternately("abcd", "pq"))
