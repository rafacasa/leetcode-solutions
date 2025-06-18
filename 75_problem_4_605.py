from typing import List

# Accepted
# Runtime 4 ms Beats 86.64%
# Memory 18.07 MB Beats 81.92%


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        len_flowerbed = len(flowerbed)
        if n == 0:
            return True
        if len_flowerbed == 1:
            return flowerbed[0] == 0
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            cnt += 1
            flowerbed[0] = 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            cnt += 1
            flowerbed[-1] = 1
        if len_flowerbed > 2:
            for i in range(1, len_flowerbed - 1):
                if (
                    flowerbed[i] == 0
                    and flowerbed[i - 1] == 0
                    and flowerbed[i + 1] == 0
                ):
                    cnt += 1
                    flowerbed[i] = 1
        return n <= cnt


print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1))
print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 2))
print(Solution().canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))
print(Solution().canPlaceFlowers([1, 0, 0, 0, 0, 0, 1], 2))
