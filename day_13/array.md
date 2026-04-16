# Arrays

- An array is a contiguous block of data, stored in RAM as it is "a contiguous block".

## Static Arrays

- `arr = [2, 4]`

### Reading from an Array

- O(1)
- We use indexes to access the array, starting from **0**.
- Example: `arr[0] = 2`

### Writing to an Array

- Arrays are **fixed** size.
- Inserting at the end and removing from the end: O(1)
- Inserting at the beginning or removing from the beginning: O(n)
    - Shift "4" from index 1 to index 2.
    - Shift "2" from index 0 to index 1.
    - Insert "6" at index 0.
    - `arr = [6, 2, 4]`
- Inserting at the middle: O(n)
    - Shift "4" from index 1 to index 2.
    - Insert "6" at index 1.
    - `arr = [2, 6, 4]`

### Dynamic Arrays

- We have a dynamic array with size = 3.
- The length of it is 0.
- Push O(1): adding elements to the end of the array.
    - pushed 0 (i = 0).
    - pushed 4 (i = 1).
    - `arr = [0, 4]`
- A pointer is initialized that tells us what index is the last element of this array.
    - we can use it to get the length of the array.
    - the pointer now points to index 1 "value = 4".
- Pop O(1): removing elements from the end of the array.
    - pop 4 (i = 1).
    - `arr = [0]`
    - the pointer moves from index = 1 to index = 0 "value = 0".
- Push 4 and 6 --> `arr = [0, 4, 6]`
- Now, we want to push 8 but we run out of space.
    - We will create a new array with a double size of the original array.
    - Size = 6.
    - Take the values from the original array and copy them at the beginning of the new one.
    - `newArr = [0, 4, 6, 8]`.
    - We free the memory from the original array as we don't need it anymore.

## Complexity

| Operation | Big-O Time |
|---|---|
| r/w i-th element | O(1) |
| Insert/Remove End | O(1) |
| Insert Middle | O(n) |
| Remove Middle | O(n) |
