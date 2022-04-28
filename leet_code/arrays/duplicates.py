"""
Methods what we can use to finish this task:
- BruteForce
- Sorting
- Hashset

Hashset:
- Time complexity: O(n)
- Space complexity: O(n)
"""

# Main function:
def contains_duplicate(nums: list[int]) -> bool:
    """ Check if in list are duplicated ints. """

    # Check if list is not empty:
    if not len(nums):
        return False

    hashset = set()

    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False


# Tests:
assert contains_duplicate([2,14,18,22,22]) == True, "Wrong Answer"
assert contains_duplicate([1,2,3,1]) == True, "Wrong Answer"
assert contains_duplicate([1,2,3,4]) == False, "Wrong Answer"
assert contains_duplicate([1,1,1,3,3,4,3,2,4,2]) == True, "Wrong Answer"
assert contains_duplicate([]) == False, "Wrong Answer"
