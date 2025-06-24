# Accepted
# Runtime 17 ms Beats 22.14%
# Memory 18.29 MB Beats 20.60%


class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        map_nums = dict()

        for num in nums1:
            content = map_nums.get(num, list((1,)))
            map_nums[num] = content

        for num in nums2:
            content = map_nums.get(num, list((2,)))
            if 2 not in content:
                content.append(2)
            map_nums[num] = content

        lista_1 = []
        lista_2 = []

        for num, in_list in map_nums.items():
            if len(in_list) == 1:
                if in_list[0] == 1:
                    lista_1.append(num)
                else:
                    lista_2.append(num)

        return [lista_1, lista_2]


print(Solution().findDifference([1, 2, 3], nums2=[2, 4, 6]))
print(Solution().findDifference([1, 2, 3, 3], nums2=[1, 1, 2, 2]))
