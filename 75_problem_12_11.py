# Accepted
# Runtime 104 ms Beats 48.41%
# Memory 28.59 MB Beats 23.71%


class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        rigth = len(height) - 1
        current_area = rigth * min(height[left], height[rigth])

        while left < rigth:
            if height[left] < height[rigth]:
                left += 1
            else:
                rigth -= 1
            current_area = max(
                current_area, (rigth - left) * min(height[left], height[rigth])
            )
        return current_area


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(Solution().maxArea([1, 1]))
print(Solution().maxArea([1, 2, 4, 3]))
print(Solution().maxArea([7, 10, 6, 2, 5, 4, 8, 3, 7]))
print(Solution().maxArea([5, 4, 3, 2, 1]))
