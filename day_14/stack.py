class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None

        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None

        return self.items[-1]

    def is_empty(self):
        return not self.items

    def __len__(self):
        return len(self.items)

    def __str__(self):
        if self.is_empty():
            return "Stack is empty"

        result = ["Top"]
        for item in reversed(self.items):
            result.append(str(item))
        result.append("Bottom")

        return "\n".join(result)
