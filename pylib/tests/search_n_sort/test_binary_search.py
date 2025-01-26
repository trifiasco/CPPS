from pylib.search_n_sort.binary_search import lower_bound, upper_bound, bisection_method


def test_lower_bound():
    array = [1, 2, 2, 3, 4, 4, 5]

    lower_bound_of_2 = lower_bound(array, 2)
    assert lower_bound_of_2 == 1

    lower_bound_of_3 = lower_bound(array, 3)
    assert lower_bound_of_3 == 3

    lower_bound_of_6 = lower_bound(array, 6)
    assert lower_bound_of_6 == 7


def test_upper_bound():
    array = [1, 2, 2, 3, 4, 4, 5]

    upper_bound_of_2 = upper_bound(array, 2)
    assert upper_bound_of_2 == 3

    upper_bound_of_3 = upper_bound(array, 3)
    assert upper_bound_of_3 == 4

    upper_bound_of_6 = upper_bound(array, 6)
    assert upper_bound_of_6 == 7


def test_bisection_method():
    assert round(bisection_method(9)) == 3.0
    assert round(bisection_method(10), 8) == 3.16227766
    assert round(bisection_method(8), 4) == 2.8284
