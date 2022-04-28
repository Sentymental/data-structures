"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice. You can return the
answer in any order.
"""

# Main Function:
def sum_two(nums: list[int], target: int):
    """Sum two numbers from list and reach the target"""

    if not len(nums) or target == 0:
        return False

    hashmap: dict = dict()

    for i, v in enumerate(nums):
        result = target - v

        if result in hashmap:
            return [hashmap[result], i]

        else:
            hashmap[v] = i

    return False


# Tests:
assert sum_two([2, 1, 5, 3], 4) == [1, 3], "Wrong Answer"
assert sum_two([], 123) == False, "Wrong Answer"
assert sum_two([], 0) == False, "Wrong Answer"
assert sum_two([2, 1, 5, 3], 123) == False, "Wrong Answer"
