"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice. You can return the
answer in any order.
"""


# Test cases:
arr = [2, 1, 5, 3]

def sum_two(nums: list[int], target: int) -> list[int]:
    """ Sum two numbers from list and reach the target """

    hashmap = dict()

    for i, v in enumerate(nums):
        result = target - v
        if result in hashmap:
            return [hashmap[result], i]
        else:
            hashmap[v] = i

    return


# Tests:
assert sum_two(arr, 4) == [1, 3], "Wrong Answer"
