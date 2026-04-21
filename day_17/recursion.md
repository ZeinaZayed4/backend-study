# Recursion

- A function calling itself with:
    1. Base case: stopping condition(s).
    2. Recursive case: problem broken into smaller sub-problems.


## One-Branch

- Each call makes one recursive call.
- Time complexity: O(n)
- Space complexity: O(n)
- Factorial **O(n)**: 
    - n! = n * (n - 1) * (n - 2) ... 1
    - n! = n * (n - 1)!
    ```py
    def factorial(n):
    # base case
    if n <= 1:
        return 1
    
    # recursive case
    return n * factorial(n - 1)
    ```

## Two-Branch

- Each call makes two recursive calls.
- Time complexity: O(2<sup>n</sup>)
- Space complexity: O(n)
- Fibonacci Number:
    - F(n) = F(n - 1) + F(n - 2)
    - F(0) = 0
    - F(1) = 1
    ```py
    def fibonacci(n):
    if n <= 1:
        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)
    ```
- Fibonacci Memo:
    ```py
    def fibonacci_memo(n, memo={}):
        if n <= 1:
            return n
        if n in memo:
            return memo[n]
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
        return memo[n]
    ```

## Factorial (recursion, iterative, reduce())

- 
    ```py
    from timeit import timeit

    setup_string = """
    print("Recursive:")
    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n - 1)
    """
    print(timeit("factorial(5)", setup=setup_string, number=10000000))

    setup_string = """
    print("Iterative:")
    def factorial(n):
        return_value = 1
        for i in range(2, n + 1):
            return_value *= i
        return return_value
    """
    print(timeit("factorial(5)", setup=setup_string, number=10000000))

    setup_string = """
    from functools import reduce
    print("reduce():")
    def factorial(n):
        return reduce(lambda x, y: x * y, range(1, n + 1) or [1])
    """
    print(timeit("factorial(5)", setup=setup_string, number=10000000))

    ```
