# Accepted
# Runtime 0 ms Beats 100.00%
# Memory 18.77 MB Beats 42.99%


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dicionario = {}
        for i, num in enumerate(nums):
            dicionario[num] = i

        for j, num2 in enumerate(nums):
            necessario = target - num2

            if necessario in dicionario and dicionario[necessario] != j:
                return [j, dicionario[necessario]]
        return []
