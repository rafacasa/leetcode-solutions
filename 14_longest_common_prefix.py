# Accepted
# Runtime 0 ms Beats 100.00%
# Memory 17.95 MB Beats 30.26%


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        size = min([len(s) for s in strs])
        prefix = ""
        for i in range(size):
            letter = None

            for word in strs:
                if letter is None:
                    letter = word[i]
                if letter != word[i]:
                    return prefix

            prefix += letter
        return prefix
