class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.size += 1
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = node
        self.size += 1

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.head is None

    def search(self, data):
        current, idx = self.head, 0

        while current:
            if current.data == data:
                return idx
            current = current.next
            idx += 1
        
        return -1

    def delete(self, data):
        current, previous = self.head, None

        while current:
            if current.data == data:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                self.size -= 1
                return True
            previous = current
            current = current.next

        return False

    def __str__(self):
        if self.head is None:
            return "LinkedList is empty"
        
        result = []
        current = self.head

        while current:
            result.append(str(current.data))
            current = current.next

        return " -> ".join(result) + " -> None"
