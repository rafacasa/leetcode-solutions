import string
from collections import deque

# Accepted
# Runtime 0 ms Beats 100.00%
# Memory 17.74 MB Beats 55.30%


class Solution:
    def decodeString(self, s: str) -> str:
        ans = ""
        temp_num = []
        temp_str = []
        stack_cnts = deque()
        stack_strs = deque()
        for char in s:
            if char in string.digits:
                if not temp_num and (stack_cnts or temp_str):
                    stack_strs.append(temp_str)
                    temp_str = list()
                temp_num.append(char)
                continue
            if char == "[":
                times = int("".join(temp_num))
                temp_num = list()
                stack_cnts.append(times)
                continue
            if char == "]":
                aux_str = "".join(temp_str) * stack_cnts.pop()
                if stack_strs:
                    temp_str = stack_strs.pop()
                    temp_str.append(aux_str)
                else:
                    ans += aux_str
                    temp_str = list()
                continue

            temp_str.append(char)

        if temp_str:
            aux_str = "".join(temp_str)
            ans += aux_str

        return ans


print(Solution().decodeString("3[a]2[bc]"))
print(Solution().decodeString("3[a2[c]]"))
print(Solution().decodeString("2[abc]3[cd]ef"))
print(Solution().decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
print(Solution().decodeString("abc3[cd]xyz"))
print(Solution().decodeString("3[a10[bc]]"))
