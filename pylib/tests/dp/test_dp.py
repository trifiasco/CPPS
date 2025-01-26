from pylib.dp.dp import (
    LCS,
    fib_basic,
    fib_cache,
    fib_custom,
    fib_lru,
    grid_paths,
    knapsack,
)
import time


def test_fibonacci():
    fib = fib_basic(10)
    assert fib == 55

    fib = fib_cache(10)
    assert fib == 55

    fib = fib_lru(10)
    assert fib == 55

    fib = fib_custom(10)
    assert fib == 55

    print("benchmark_results")
    benchmark_fibonacci(10)


def test_lcs():
    lcs = LCS()
    result = lcs.longest_common_subsequence("ABCDGH", "AEDFHR")
    assert result == "ADH"


def test_knap_sack():
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 8
    result = knapsack(weights, values, capacity)
    assert result == 10


def test_grid_path():
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

    result = grid_paths(grid)
    assert result == 7


def benchmark_fibonacci(n: int = 35) -> None:
    """Benchmark different Fibonacci implementations."""
    implementations = [
        ("Basic Recursive", fib_basic),
        ("Built-in Cache", fib_cache),
        ("LRU Cache", fib_lru),
        ("Custom Memoize", fib_custom),
    ]

    for name, func in implementations:
        start_time = time.time()
        result = func(n)
        end_time = time.time()
        print(f"{name:15} -> Time: {end_time - start_time:.4f}s, Result: {result}")
