# Accepted
# Runtime 18 ms Beats 30.41%
# Memory 18.58 MB Beats 68.90%


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
        ans = list(s)
        n = len(s)
        i, j = 0, n - 1

        while i < j:
            i_vowel = s[i] in vowels
            j_vowel = s[j] in vowels
            if i_vowel and j_vowel:
                temp = ans[i]
                ans[i] = ans[j]
                ans[j] = temp
                i += 1
                j -= 1
            if not i_vowel:
                i += 1
            if not j_vowel:
                j -= 1

        return "".join(ans)


print(Solution().reverseVowels("IceCreAm"))
print(Solution().reverseVowels("leetcode"))
