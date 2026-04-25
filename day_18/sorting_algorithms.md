# Sorting Algorithms

## Bubble Sort

- `arr = [8, 5, 7, 3, 2]`, n = 5
- **1<sup>st</sup> pass:**
    |   |   |   |   |   |
    |---|---|---|---|---|
    | 8 | 5 | 5 | 5 | 5 |
    | 5 | 8 | 7 | 7 | 7 |
    | 7 | 7 | 8 | 3 | 3 |
    | 3 | 3 | 3 | 8 | 2 |
    | 2 | 2 | 2 | 2 | 8 |
    - 4 comparisons.
    - 4 swaps.
- **2<sup>nd</sup> pass:**
    |   |   |   |
    |---|---|---|
    | 5 | 5 | 5 |
    | 7 | 3 | 3 |
    | 3 | 7 | 2 |
    | 2 | 2 | 7 |
    | 8 | 8 | 8 |
    - 3 comparisons.
    - 3 swaps.
- **3<sup>rd</sup> pass:**
    |   |   |   |
    |---|---|---|
    | 5 | 3 | 3 |
    | 3 | 5 | 2 |
    | 2 | 2 | 5 |
    | 7 | 7 | 7 |
    | 8 | 8 | 8 |
    - 2 comparisons.
    - 2 swaps.
- **4<sup>th</sup> pass:**
    |   |   |
    |---|---|
    | 3 | 2 |
    | 2 | 3 |
    | 5 | 5 |
    | 7 | 7 |
    | 8 | 8 |
    - 1 comparison.
    - 1 swap.
- No.of passes = (n - 1) passes.
- No.of comparisons = n(n - 1)/2 = O(n<sup>2</sup>)
- Max no.of swaps = n(n - 1)/2 = O(n<sup>2</sup>)
- **Bubble sort is adaptive(if optimized) and stable.**
- Bubble sort time:
    |   |   |
    |---|---|
    | Min | O(n) |
    | Max | O(n<sup>2</sup>) |

## Selection Sort

- Selection sort time: **O(n<sup>2</sup>)**

    |     |     |     |     |     |     |     |     |     | | min | temp |
    |-----|-----|-----|-----|-----|-----|-----|-----|-----|-|:---:|:----:|
    |  9  |  1  |  8  |  2  |  7  |  3  |  6  |  4  |  5  | |  1  |   9  |
    |**1**|**9**|  8  |  2  |  7  |  3  |  6  |  4  |  5  | |  2  |   9  |
    |  1  |**2**|  8  |**9**|  7  |  3  |  6  |  4  |  5  | |  3  |   8  |
    |  1  |  2  |**3**|  9  |  7  |**8**|  6  |  4  |  5  | |  4  |   9  |
    |  1  |  2  |  3  |**4**|  7  |  8  |  6  |**9**|  5  | |  5  |   7  |
    |  1  |  2  |  3  |  4  |**5**|  8  |  6  |  9  |**7**| |  6  |   8  |
    |  1  |  2  |  3  |  4  |  5  |**6**|**8**|  9  |  7  | |  7  |   8  |
    |  1  |  2  |  3  |  4  |  5  |  6  |**7**|  9  |**8**| |  8  |   9  |
    |  1  |  2  |  3  |  4  |  5  |  6  |  7  |**8**|**9**| |     |      |

## Insertion Sort

- Inserting an element into a sorted array in a sorted position.
- Insertion sort is stable.
- Insertion sort time:
    |   |   |
    |---|---|
    | Min | O(n) |
    | Max | O(n<sup>2</sup>) |
- Ex: `a = [2, 6, 10, 15, 20, 25, 30]`, insert 12
    | 2 | 6 | 10 | 15 | 20 | 25 | 30 |    |
    |---|---|----|----|----|----|----|----|
    | 2 | 6 | 10 | 15 | 20 | 25 |    | 30 |
    | 2 | 6 | 10 | 15 | 20 |    | 25 | 30 |
    | 2 | 6 | 10 | 15 |    | 20 | 25 | 30 |
    | 2 | 6 | 10 |    | 15 | 20 | 25 | 30 |
    | 2 | 6 | 10 | 12 | 15 | 20 | 25 | 30 |
- Result: `a = [2, 6, 10, 12, 15, 20, 25, 30]`
