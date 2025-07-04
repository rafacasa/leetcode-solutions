# Accepted
# Runtime 2725 ms Beats 78.02%
# Memory 26.03 MB Beats 64.84%


MOD = 10**9 + 7


class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        cnts = []
        curr_cnt = 1

        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                curr_cnt += 1
            else:
                cnts.append(curr_cnt)
                curr_cnt = 1
        cnts.append(curr_cnt)

        total_str = 1
        for cnt in cnts:
            total_str = (total_str * cnt) % MOD

        if k <= len(cnts):
            return total_str

        dp = [0] * k
        dp[0] = 1

        for cnt in cnts:
            temp = [0] * k
            sum_strs = 0

            for i in range(1, k):
                sum_strs = (sum_strs + dp[i - 1]) % MOD
                if i > cnt:
                    sum_strs = (sum_strs - dp[i - cnt - 1] + MOD) % MOD
                temp[i] = sum_strs
            dp = temp

        sum_invalids = sum(dp[len(cnts) : k]) % MOD
        return (total_str - sum_invalids + MOD) % MOD


print(Solution().possibleStringCount("aabbccdd", k=7))
print(Solution().possibleStringCount("aabbccdd", k=8))
print(Solution().possibleStringCount("aaabbb", k=3))
