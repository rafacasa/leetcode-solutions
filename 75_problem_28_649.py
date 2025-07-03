from collections import deque

# Accepted
# Runtime 19 ms Beats 33.21%
# Memory 18.01 MB Beats 72.49%


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        last_ltr = ""
        cnt_bans = 0
        queue = deque(senate)

        while len(queue) > 1 and cnt_bans < len(queue):
            l = queue.popleft()
            if not last_ltr:
                last_ltr = l
            if last_ltr == l:
                cnt_bans += 1
                queue.append(l)
            else:
                if cnt_bans:
                    cnt_bans -= 1
                else:
                    last_ltr = l
                    cnt_bans = 1
                    queue.append(l)

        winner = queue.popleft()
        if winner == "R":
            return "Radiant"
        return "Dire"


print(Solution().predictPartyVictory("RD"))
print(Solution().predictPartyVictory("RDD"))
