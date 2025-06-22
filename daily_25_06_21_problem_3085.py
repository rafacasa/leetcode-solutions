# Accepted
# Runtime 92 ms Beats 28.68%
# Memory 17.90 MB Beats 100.00%


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt_letters = {}
        deletions = []

        for letter in word:
            cnt = cnt_letters.get(letter, 0)
            cnt_letters[letter] = cnt + 1

        for cnt in cnt_letters.values():
            delete = 0
            limit = cnt + k
            for cnt_other in cnt_letters.values():
                if cnt_other < cnt:
                    delete += cnt_other
                if cnt_other > limit:
                    delete += cnt_other - limit
            deletions.append(delete)

        return min(deletions)


print(Solution().minimumDeletions("aabcaba", 0))
print(Solution().minimumDeletions("dabdcbdcdcd", 2))
print(Solution().minimumDeletions("aaabaaa", 2))
print(Solution().minimumDeletions("zzfzzzzppfp", 1))
