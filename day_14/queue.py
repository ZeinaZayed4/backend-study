from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.popleft()

    def is_empty(self):
        return not self.items

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def __str__(self):
        if self.is_empty():
            return "Queue is empty"

        result = ["Front"]
        for item in self.items:
            result.append(str(item))
        result.append("Back")

        return "\n".join(result)
