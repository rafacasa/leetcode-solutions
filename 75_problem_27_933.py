from collections import deque

# Accepted
# Runtime 47 ms Beats 41.21%
# Memory 22.95 MB Beats 93.21%


class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

a = RecentCounter()
print(a.ping(1))
print(a.ping(100))
print(a.ping(3001))
print(a.ping(3002))
