# Accepted
# Runtime 2143 ms Beats 85.94%
# Memory 17.97 MB Beats 94.53%


class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans = 0
        north = south = west = east = 0

        for direction in s:
            if direction == "N":
                north += 1
            elif direction == "S":
                south += 1
            elif direction == "E":
                east += 1
            elif direction == "W":
                west += 1

            modifications_horizontal = min(west, east, k)
            modifications_vertical = min(north, south, k - modifications_horizontal)

            distance_horizontal = abs(west - east) + modifications_horizontal * 2
            distance_vertical = abs(north - south) + modifications_vertical * 2

            ans = max(ans, distance_horizontal + distance_vertical)

        return ans


print(Solution().maxDistance("NWSE", 1))
print(Solution().maxDistance("NSWWEW", 3))
