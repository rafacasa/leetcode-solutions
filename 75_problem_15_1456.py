# Accepted
# Runtime 75 ms Beats 69.87%
# Memory 17.95 MB Beats 88.20%


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        left = 0
        right = k
        cnt_vowels = 0

        for letter in s[0:right]:
            if letter in vowels:
                cnt_vowels += 1

        max_vowels = cnt_vowels

        while right < len(s):
            if s[left] in vowels:
                cnt_vowels -= 1
            if s[right] in vowels:
                cnt_vowels += 1
            max_vowels = max(max_vowels, cnt_vowels)
            left += 1
            right += 1
        return max_vowels


print(Solution().maxVowels("abciiidef", k=3))
print(Solution().maxVowels("aeiou", k=2))
print(Solution().maxVowels("leetcode", k=3))
