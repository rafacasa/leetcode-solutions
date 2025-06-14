from collections import deque
from typing import List

# Accepted
# Runtime 19 ms Beats 49.18%
# Memory 28.25 MB Beats 24.54%


class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:
        queue = deque()
        locked_boxes = deque()
        # cnt_locked = 0
        cnt_candies = 0
        queue.extend(initialBoxes)

        while queue:
            box = queue.popleft()
            if status[box]:
                cnt_candies += candies[box]
                for key in keys[box]:
                    status[key] = 1
                    if key in locked_boxes:
                        locked_boxes.remove(key)
                        queue.append(key)
                for box_found in containedBoxes[box]:
                    queue.append(box_found)
            else:
                locked_boxes.append(box)

        return cnt_candies


print(
    Solution().maxCandies(
        [1, 0, 1, 0], [7, 5, 4, 100], [[], [], [1], []], [[1, 2], [3], [], []], [0]
    )
)

print(
    Solution().maxCandies(
        [1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1],
        [[1, 2, 3, 4, 5], [], [], [], [], []],
        [[1, 2, 3, 4, 5], [], [], [], [], []],
        [0],
    )
)

print(
    Solution().maxCandies(
        [1, 0, 1, 0, 0],
        [7, 5, 4, 100, 4],
        [[], [], [3], [1], []],
        [[1, 2], [], [3, 4], [], []],
        [0],
    )
)
