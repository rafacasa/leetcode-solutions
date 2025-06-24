# Accepted
# Runtime 135 ms Beats 49.12%
# Memory 18.30 MB Beats 45.94%


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        letters1 = set(word1)
        letters2 = set(word2)

        if letters2 != letters1:
            return False

        cnt_chars_1 = {}

        for letter in word1:
            cnt = cnt_chars_1.get(letter, 0)
            cnt_chars_1[letter] = cnt + 1

        cnt_chars_2 = {}

        for letter in word2:
            cnt = cnt_chars_2.get(letter, 0)
            cnt_chars_2[letter] = cnt + 1

        list_cnt_chars_1 = [c for c in cnt_chars_1.values()]
        list_cnt_chars_1.sort()
        list_cnt_chars_2 = [c for c in cnt_chars_2.values()]
        list_cnt_chars_2.sort()

        return list_cnt_chars_1 == list_cnt_chars_2


print(Solution().closeStrings("abc", word2="bca"))
print(Solution().closeStrings("a", word2="aa"))
print(Solution().closeStrings("cabbba", word2="abbccc"))
