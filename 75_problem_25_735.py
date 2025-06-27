from collections import deque

# Accepted
# Runtime 3 ms Beats 93.73%
# Memory 18.80 MB Beats 86.89%


class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        ans = list()
        stack = deque()

        for ast in asteroids:
            if ast > 0:
                stack.append(ast)
                continue

            if len(stack) == 0:
                ans.append(ast)
                continue

            while stack[-1] <= abs(ast):
                out = stack.pop()
                if out == abs(ast):
                    break
                if len(stack) == 0:
                    ans.append(ast)
                    break

        for ast in stack:
            ans.append(ast)

        return ans


print(Solution().asteroidCollision([5, 10, -5]))
print(Solution().asteroidCollision([8, -8]))
print(Solution().asteroidCollision([10, 2, -5]))
