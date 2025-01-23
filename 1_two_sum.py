class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicionario = {}
        for i, num in enumerate(nums):
            dicionario[num] = i
        
        for j, num2 in enumerate(nums):
            necessario = target - num2

            if necessario in dicionario and dicionario[necessario] != j:
                return [j, dicionario[necessario]]
        return []
