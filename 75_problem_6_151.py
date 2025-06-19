# Accepted
# Runtime 0 ms Beats 100.00%
# Memory 18.14 MB Beats 5.00%


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        return " ".join(words[::-1])


print(Solution().reverseWords("the sky is blue"))
print(Solution().reverseWords("  hello world  "))
print(Solution().reverseWords("a good   example"))
