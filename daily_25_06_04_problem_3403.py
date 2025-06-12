# Accepted
# Runtime 16 ms Beats 38.41%
# Memory 17.91 MB Beats 42.14%


class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        size_sstr = n - numFriends + 1
        start = 0
        end = size_sstr
        ans = ""
        while start < n:
            ans = max(ans, word[start:end])
            start += 1
            if end <= n:
                end += 1
        return ans


print(Solution().answerString("dbca", 2))
print(Solution().answerString("gggg", 4))
print(Solution().answerString("aann", 2))
