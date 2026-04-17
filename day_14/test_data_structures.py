import pytest

from linked_list import LinkedList
from queue import Queue
from stack import Stack


class TestLinkedList:
    def test_append_to_empty(self):
        ll = LinkedList()
        ll.append(2)
        assert len(ll) == 1
        assert ll.search(2) == 0

    def test_append_multiple(self):
        ll = LinkedList()
        ll.append(2)
        ll.append(4)
        ll.append(6)
        assert len(ll) == 3
        assert str(ll) == "2 -> 4 -> 6 -> None"

    def test_delete_head(self):
        ll = LinkedList()
        ll.append(2)
        ll.append(4)
        assert ll.delete(2) == True
        assert len(ll) == 1
        assert str(ll) == "4 -> None"

    def test_delete_not_found(self):
        ll = LinkedList()
        ll.append(2)
        assert ll.delete(4) == False
        assert len(ll) == 1

    def test_search(self):
        ll = LinkedList()
        ll.append(2)
        ll.append(4)
        assert ll.search(4) == 1
        assert ll.search(8) == -1


class TestQueue:
    def test_enqueue_dequeue(self):
        q = Queue()
        q.enqueue(2)
        q.enqueue(4)
        assert q.dequeue() == 2
        assert q.dequeue() == 4
        assert q.is_empty()

    def test_peek(self):
        q = Queue()
        q.enqueue(2)
        q.enqueue(4)
        assert q.peek() == 2

    def test_dequeue_empty(self):
        q = Queue()
        assert q.dequeue() is None


class TestStack:
    def test_push_pop(self):
        s = Stack()
        s.push(2)
        s.push(4)
        assert s.pop() == 4
        assert s.pop() == 2
        assert s.is_empty

    def test_peek(self):
        s = Stack()
        s.push(2)
        assert s.peek() == 2
        assert len(s) == 1

    def test_pop_empty(self):
        s = Stack()
        assert s.pop() is None
