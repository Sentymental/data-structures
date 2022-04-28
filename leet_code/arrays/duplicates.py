"""
Methods what we can use to finish this task:
- BruteForce
- Sorting
- Hashset

Hashset:
- Time complexity: O(n)
- Space complexity: O(n)
"""

# Test cases:
arr = [2,14,18,22,22]
arr1 = [1,2,3,1]
arr2 = [1,2,3,4]
arr3 = [1,1,1,3,3,4,3,2,4,2]


# Main function:
def contains_duplicate(nums: list[int]) -> bool:
    hashset = set()

    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False


# Tests:
assert contains_duplicate(arr) == True
assert contains_duplicate(arr1) == True
assert contains_duplicate(arr2) == False
assert contains_duplicate(arr3) == True
