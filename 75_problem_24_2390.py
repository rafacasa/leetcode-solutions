from collections import deque

# Accepted
# Runtime 98 ms Beats 57.61%
# Memory 19.24 MB Beats 25.33%


class Solution:
    def removeStars(self, s: str) -> str:
        stack = deque()

        for letter in s:
            if letter == "*":
                stack.pop()
            else:
                stack.append(letter)

        return "".join(stack)


print(Solution().removeStars("leet**cod*e"))
print(Solution().removeStars("erase*****"))
