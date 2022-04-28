"""
Given an array of sorted integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly
one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

# Test Cases:
arr = [2, 7, 11, 15]
arr1 = [2, 3, 4]
arr2 = [1, 3, 4, 5, 7, 10, 11]


# Main Function
def sum_two(arr: list[int], target: int) -> list[int]:
    """
    Sum Two function returns indexes of two
    intergers that sums to the target
    """
    start, end = 0, len(arr) - 1

    while start < end:
        result = arr[start] + arr[end]

        if result > target:
            end -= 1

        elif result < target:
            start += 1

        else:
            return [start, end]

    return []


# Tests:
assert sum_two(arr, 9) == [0, 1], "Wrong"
assert sum_two(arr1, 6) == [0, 2], "Wrong"
assert sum_two(arr2, 9) == [2, 3], "Wrong"
