from collections import deque


class Solution1:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue


class Solution2:

    def __init__(self):
        self.queue = None

    def push(self, x: int) -> None:
        self.queue2 = deque()
        self.queue2.append(x)
        self.queue2.append(self.queue)
        self.queue = self.queue2

    def pop(self) -> int:
        val, self.queue = self.queue.popleft(), self.queue.popleft()
        return val

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue
