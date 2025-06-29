class Solution:
    def count_prefix(self, word1, word2):
        cnt = 0
        for i in range(min(len(word1), len(word2))):
            if word1[i] == word2[i]:
                cnt += 1
            else:
                return cnt
        return cnt

    def longestCommonPrefix(self, words: list[str]) -> list[int]:
        max_prefix = 0
        i_max_prefix = 0
        i2_max_prefix = 0
        second_max_prefix = 0
        for i_adjacent in range(len(words) - 1):
            i_2 = i_adjacent + 1
            prefix = self.count_prefix(words[i_adjacent], words[i_2])
            if prefix > max_prefix:
                second_max_prefix = max_prefix
                max_prefix = prefix
                i_max_prefix = i_adjacent
                i2_max_prefix = i_2
            elif prefix > second_max_prefix:
                second_max_prefix = prefix

        return [
            (
                max_prefix
                if i != i_max_prefix and i != i2_max_prefix
                else second_max_prefix
            )
            for i in range(len(words))
        ]


print(Solution().longestCommonPrefix(["jump", "run", "run", "jump", "run"]))
print(Solution().longestCommonPrefix(["dog", "racer", "car"]))
print(Solution().longestCommonPrefix(["fec", "fef", "acaa", "adfa", "afc", "fdbda"]))
print(
    Solution().longestCommonPrefix(
        [
            "f",
            "cfe",
            "feab",
            "fcc",
            "cdfda",
            "fcec",
            "afae",
            "cdeb",
            "dc",
            "bffd",
            "edabe",
        ]
    )
)
