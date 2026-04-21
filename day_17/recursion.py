def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)


def reverse_string(s):
    if not s:
        return ""
    return s[-1] + reverse_string(s[:-1])


def count_occurrences(arr: list, target):
    if not arr:
        return 0
    return (target == arr[-1]) + count_occurrences(arr[:-1], target)


def is_palindrome(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])
