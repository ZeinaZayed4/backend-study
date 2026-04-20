# Linked Lists

- We can't just arbitrary access the second/third .. nth element, we have to follow pointers to do that.

- Complexity:
    | | Arrays | Linked Lists |
    | Operation | Big-O Time | |
    |---|---|---|
    | Access i-th element | O(1) | O(n) |
    | Insert/remove end | O(1) | O(1) |
    | Insert/remove middle | O(n) | O(n) |

## Singly Linked Lists

- Linked lists are made of **Nodes** which encapsulates two things at a minimum:
    - **value:** it could be anything "int, char, etc.."
    - **next:** a pointer to the next node in the linked list.
- Linked lists' nodes are not stored in memory as a contiguous block, they could be in some random order connected via pointers.

- Looping through the linked list **O(n)**:
    ```
    cur = ListNode1
    while (cur != null)
        cur = cur.next
    ```
- Adding new node to the end "we have two pointers _head and tail_" **O(1)**:
    ```
    tail.next = NewNode
    tail = tail.next
    // or: tail = NewNode
    ```
- Deleting an existing node **O(n)**:
    - For the second element O(1)
        ```
        head.next = head.next.next
        ```

## Doubly Linked Lists

- In doubly linked lists we have two pointers _previous_ and _next_ and the value.

- Adding a new node to the end **O(1)**:
    ```
    tail.next = NewNode
    NewNode.prev = tail
    tail = tail.next
    // or tail = NewNode
    ```
- Removing the last node **O(1)**:
    ```
    tail.prev.next = null
    tail = tail.prev
    ```
