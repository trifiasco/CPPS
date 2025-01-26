from functools import cache, lru_cache, wraps
from typing import Callable, cast
import sys

MAX_INT = sys.maxsize


# Example 1: Fibonacci with different memoization techniques
def fib_basic(n: int) -> int:
    """Basic recursive Fibonacci without memoization."""
    if n <= 1:
        return n
    return fib_basic(n - 1) + fib_basic(n - 2)


@cache  # Built-in cache decorator (Python 3.9+)
def fib_cache(n: int) -> int:
    """Fibonacci with built-in cache decorator."""
    if n <= 1:
        return n
    return fib_cache(n - 1) + fib_cache(n - 2)


@lru_cache(maxsize=128)  # LRU cache with size limit
def fib_lru(n: int) -> int:
    """Fibonacci with LRU cache decorator."""
    if n <= 1:
        return n
    return fib_lru(n - 1) + fib_lru(n - 2)


def memoize[T, **P](func: Callable[P, T]) -> Callable[P, T]:
    """
    Custom memoization decorator with type hints.
    Caches results of function calls.
    """
    cache: dict[tuple, T] = {}

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        # Create a cache key from both positional and keyword arguments
        key = (*args, *sorted(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper


@memoize
def fib_custom(n: int) -> int:
    """Fibonacci with custom memoization decorator."""
    if n <= 1:
        return n
    return fib_custom(n - 1) + fib_custom(n - 2)


# ==================================================================================================
# Example 2: Longest Common Subsequence with class-based memoization
class LCS:
    def __init__(self) -> None:
        self.memo: dict[tuple[int, int], str] = {}

    def longest_common_subsequence(self, text1: str, text2: str) -> str:
        """Find the longest common subsequence of two strings."""

        def dp(i: int, j: int) -> str:
            if i == len(text1) or j == len(text2):
                return ""

            key = (i, j)
            if key in self.memo:
                return self.memo[key]

            if text1[i] == text2[j]:
                result = text1[i] + dp(i + 1, j + 1)
            else:
                option1 = dp(i + 1, j)
                option2 = dp(i, j + 1)
                result = option1 if len(option1) > len(option2) else option2

            self.memo[key] = result
            return result

        return dp(0, 0)


# Example 3: Knapsack with typed dictionary memoization
def knapsack(weights: list[int], values: list[int], capacity: int) -> int:
    """
    Solve the 0/1 knapsack problem using dynamic programming.
    Returns the maximum value that can be achieved.
    """
    memo: dict[tuple[int, int], int] = {}

    def dp(index: int, remaining_capacity: int) -> int:
        if index >= len(weights) or remaining_capacity <= 0:
            return 0

        key = (index, remaining_capacity)
        if key in memo:
            return memo[key]

        # Don't take current item
        result = dp(index + 1, remaining_capacity)

        # Take current item if possible
        if weights[index] <= remaining_capacity:
            result = max(
                result,
                values[index] + dp(index + 1, remaining_capacity - weights[index]),
            )

        memo[key] = result
        return result

    return dp(0, capacity)


# Example 4: Grid paths with 2D array memoization
def grid_paths(grid: list[list[int]]) -> int:
    """
    Find the minimum path sum from top-left to bottom-right in a grid.
    """
    rows, cols = len(grid), len(grid[0])
    memo: list[list[int | None]] = [[None] * cols for _ in range(rows)]

    def dp(i: int, j: int) -> int:
        if i == rows - 1 and j == cols - 1:
            return grid[i][j]
        if i >= rows or j >= cols:
            return MAX_INT

        if memo[i][j] is not None:
            return cast(int, memo[i][j])

        memo[i][j] = grid[i][j] + min(dp(i + 1, j), dp(i, j + 1))
        return cast(int, memo[i][j])

    return dp(0, 0)
