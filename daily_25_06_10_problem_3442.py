# Accepted
# Runtime 3 ms Beats 64.78%
# Memory 17.78 MB Beats 76.29%


class Solution:
    def maxDifference(self, s: str) -> int:
        letters = dict()
        for letter in s:
            try:
                letters[letter] += 1
            except KeyError:
                letters[letter] = 1

        max_odd = 0
        min_even = 101

        for qtd in letters.values():
            if qtd % 2 == 0:
                if qtd < min_even:
                    min_even = qtd
            else:
                if qtd > max_odd:
                    max_odd = qtd

        return max_odd - min_even


print(Solution().maxDifference("aaaaabbc"))
print(Solution().maxDifference("abcabcab"))
print(Solution().maxDifference("mmsmsym"))
