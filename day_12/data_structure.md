# Data Structure

## What is a Data Structure (DS)?

- A way of organizing data so that it can be used effectively.

## Why Data Structures?

- They are essential ingredients in creating fast and powerful algorithms.
- They help to manage and organize data.
- They make code cleaner and easier to understand.

## Abstract Data Type

- ADT is an abstraction of a data structure which provides only the interface to which a data structure must adhere to.
- The interface doesn't give any specific details about how something should be implemented or in what programming language.
- Examples: 
    | Abstraction (ADT) | Implementation (DS) |
    |---|---|
    | List | Dynamic Array - Linked List |
    | Queue | Linked List based Queue - Array based Queue - Stack based Queue|
    | Map | Tree Map - Hash Map / Hash Table |
    | Vehicle | Golf Cart - Bicycle - Smart Car |

## Computational Complexity Analysis

- There are two questions we ask all time:
    - How much **time** does this algorithm need to finish?
    - How much **space** does this algorithm need for its computation?

### Big-O Notation

- gives an upper bound of the complexity in the **worst** case, helping to quantify performance as the input size becomes **arbitrarily large**.
- n: the size of the input.
- Complexities ordered in from smallest to largest:
    - Constant time: **O(1)**
    - Logarithmic time: **O(log(n))**
    - Linear time: **O(n)**
    - Linearithmic time: **O(nlog(n))**
    - Quadric time: **O(n<sup>2</sup>)**
    - Cubic time: **O(n<sup>3</sup>)**
    - Exponential time: **O(b<sup>n</sup>)**, b > 1
    - Factorial time: **O(n!)**

### Big-O Properties

- O(n + c) = O(n)
- O(cn) = O(n), c > 0
- Let f be a function that describes the running time of a particular algorithm for an input of size n:
    - f(n) = 7log(n)<sup>3</sup> + 15n<sup>2</sup> + 2n<sup>3</sup> + 8
    - O(f(n)) = O(n<sup>3</sup>)

### Big-O Examples

- The following run in _constant_ time: O(1)
    - `a := 1`
    - `b := 2`
    - `c := a + 5*b`
    - ```
      i := 0
      While i < 11 Do
          i = i + 1
- The following run in _linear_ time: O(n)
    - f(n) = n --> O(f(n)) = O(n)
        ```
        i := 0
        While i < n Do
            i = i + 1
    - f(n) = n/3 --> O(f(n)) = O(n)
        ```
        i := 0
        While i < n Do
            i = i + 3
- Both of the following run in _quadratic_ time: O(n<sup>2</sup>)
    - f(n) = n*n = n<sup>2</sup> --> O(f(n)) = O(n<sup>2</sup>)
        ```
        For (i := 0; i < n; i = i + 1)
            For (j := 0; j < n; j = j + 1)
    - O(n(n+1)/2) = O(n<sup>2</sup>/2 + n/2) =  O(n<sup>2</sup>)
        ```
        For (i := 0; i < n; i = i + 1)
            For (j := i; j < n; j = j + 1)
    - i goes from [0, n), remark that if i=0, we do know n work, if i=1, we do n-1 work, if i=2, we do n-2 work, etc..
    - So, the question becomes what is: (n) + (n-1) + (n-2) + ... + 2 + 1?
        - This turns out to be n(n+1)/2
- Suppose we have a sorted array and we want to find the index of a particular value in the array, if it exists. What is the time complexity of the following algorithm?
    - ```
      low := 0
      high := n - 1
      While low <= high Do

        mid := (low + high) / 2

        If array[mid] == value: return mid
        Else If array[mid] < value: lo = mid + 1
        Else If array[mid] > value: hi = mid - 1
      return -1 // Value not found
    - Answer: O(log<sub>2</sub>(n)) = O(log(n))
- f(n) = n * (3n + 2n) = 5n<sup>2</sup> --> O(f(n)) = O(n<sup>2</sup>)
    ```
    i := 0
    While i < n Do
        j = 0
        While j < 3*n Do
            j = j + 1
        j = 0
        While j < 2*n Do
            j = j + 1
        i = i + 1
- f(n) = 3n * (40 + n<sup>3</sup>/2) = 3n/40 + 3n<sup>4</sup>/2 --> O(f(n)) = O(n<sup>4</sup>)
    ```
    i := 0
    While i < 3*n Do
        j := 10
        While j <= 50 Do
            j = j + 2
        j = 0
        While j < n*n*n Do
            j = j + 1
        i = i + 1
- Finding all subsets of a set - O(2<sup>2</sup>)
- Finding all permutations of a string - O(n!)
- Sorting using mergesort - O(nlog(n))
- Iterating over all the cells in a matrix of size n by m - O(nm)

## Static and Dynamic Arrays

### What is a Static Array?

- a fixed length container containing n elements _indexable_ from the range [0, n-1]
- indexable: each slot/index in the array can be referenced with a number.

### When and Where is a Static Array Used?

1. Storing and accessing sequential data.
2. Temporarily storing objects.
3. Used by I/O routines as buffers.
4. Lookup tables and inverse lookup tables.
5. Can be used to return multiple values from a function.
6. Used in dynamic programming to cache answers to sub-problems.

- Complexity
    || Static Array| Dynamic Array|
    |---|---|---|
    | Access | O(1) | O(1) |
    | Search | O(n) | O(n) |
    | Insertion | N/A | O(n) |
    | Appending | N/A | O(1) |
    | Deletion | N/A | O(n) |
- Static Array:
    - `A = [44, 12, -5, 17, 6, 0, 3, 9, 100]`
    - A[0] = 44     - A[4] = 6      - A[9] -> index out of bounds!
    - A[0] = -1     - A[5] = 18     - A[6] = 25
    - `A = [-1, 12, -5, 17, 6, 18, 25, 9, 100]`
- Dynamic Array:
    - The dynamic array can grow and shrink in size.
        - `A = [34, 4]`
        - A.add(-7) -> `A = [34, 4, -7]`
        - A.add(34) -> `A = [34, 4, -7, 34]`
        - A.remove(4) -> `A = [34, -7, 34]`
    - How can we implement a dynamic array?
        - One way is to use a static array.
        1. Create a static array with initial capacity.
        2. Add elements to the underlying static array, keeping track of the number of elements.
        3. If adding another element will exceed the capacity, then create a new static array with twice the capacity and copy the original elements into it.

## Singly and Doubly Linked Lists

### What is a Linked List?

- is a sequential list of nodes that hold data which point to other nodes also containing data.

### Where are Linked Lists used?

- Used in many List, Queue and Stack implementations.
- Great for creating circular lists.
- Can easily model real world objects such as trains.
- Used in separate chaining, which is present certain HashTable implementations to deal with hashing collisions.
- Often used in the implementation of adjacency lists for graphs.

### Terminology

- **Head:** the first node in a linked list.
- **Tail:** the last node in a linked list.
- **Pointer:** reference to another node.
- **Node:** an object containing data and pointer(s).

### Singly vs Doubly Linked Lists

- Singly linked lists only hold a reference to the "next" node.
- In doubly linked lists, each node holds a reference to the "next" and previous "node".
- || Pros | Cons |
  |---|---|---|
  | Singly Linked | Uses less memory | Cannot easily access previous elements. |
  || Simpler implementation ||
  | Doubly Linked | Can be traversed backwards | Takes 2x memory |

#### Inserting Singly Linked List

- Insert 11 where the third node is.
    - `5 --> 23 --> 7 --> 13`
    1. Create new pointer which points to the head "5".
    2. Move the new pointer to the second node "23".
    3. Create the new node "11", make its next pointer points to "7".
    4. Make "23" next pointer point to "11".
    - `5 --> 23 --> 11 --> 7 --> 13`

#### Inserting Doubly Linked List

- Insert 11 where the third node is.
    - `5 <--> 23 <--> 7 <--> 13`
    1. Create new pointer which points to the head "5".
    2. Move the new pointer to the second node "23".
    3. Create the new node "11", make its next pointer points to "7". and its previous pointer points to "23".
    4. Make "7" previous pointer point to "11".
    5. Make "23" next pointer point to "11".
    - `5 <--> 23 <--> 11 <--> 7 <--> 13`

#### Removing from Singly Linked List

- Remove 9 from the following SLL
    - `7 --> 0 --> 4 --> 9 --> 15`
    1. Create 2 pointers, trav1 points to the head "7", trav2 points to "0".
    2. Move the pointers until trav2 points to "9", and trav1 to the previous one.
    3. Create a new pointer "temp" which points to "9".
    4. Move trav2 to the next node of "9".
    5. Set trav1 next pointer to equal to trav2.
    6. Remove temp pointer.
    - `7 --> 0 --> 4 --> 15`

#### Removing from Doubly Linked List

- Remove 9 from the following DLL
    - `7 <--> 0 <--> 4 <--> 9 <--> 15`
    1. Create new pointer, trav points to the head "7".
    2. Move trav pointer to "9".
    5. Set "4" next pointer to equal to "15".
    6. Set "15" previous pointer to equal "4".
    6. Remove trav.
    - `7 <--> 0 <--> 4 <--> 15`

### Complexity
-
    || Singly Linked | Doubly Linked |
    |---|---|---|
    | Search | O(n) | O(n) |
    | Insert at head | O(1) | O(1) |
    | Insert at tail | O(1) | O(1) |
    | Remove at head | O(1) | O(1) |
    | Remove at tail | O(n) | O(1) |
    | Remove in middle | O(n) | O(n) |
