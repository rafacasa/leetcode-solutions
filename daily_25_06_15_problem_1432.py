# Accepted
# Runtime 0 ms Beats 100.00%
# Memory 17.64 MB Beats 88.27%


class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)
        max_num = None
        min_num = None

        if num_str[0] not in ["0", "1"]:
            min_num = int(num_str.replace(num_str[0], "1"))

        for digit in num_str:
            if not max_num and digit != "9":
                max_num = int(num_str.replace(digit, "9"))

            if not min_num and digit not in ["0", "1"]:
                min_num = int(num_str.replace(digit, "0"))

            if max_num and min_num:
                break

        if not max_num:
            max_num = num

        if not min_num:
            min_num = num

        return max_num - min_num


print(Solution().maxDiff(555))
print(Solution().maxDiff(9))
print(Solution().maxDiff(123456))
print(Solution().maxDiff(123))
print(Solution().maxDiff(111))
print(Solution().maxDiff(1101057))
