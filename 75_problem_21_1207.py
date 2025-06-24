# Accepted
# Runtime 0 ms Beats 100.00%
# Memory 17.89 MB Beats 65.40%


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        cnt = dict()

        for num in arr:
            cnt_num = cnt.get(num, 0)
            cnt[num] = cnt_num + 1

        set_cnt = {cnt_num for cnt_num in cnt.values()}
        return len(set_cnt) == len(cnt)


print(Solution().uniqueOccurrences([1, 2, 2, 1, 1, 3]))
print(Solution().uniqueOccurrences([1, 2]))
print(Solution().uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
