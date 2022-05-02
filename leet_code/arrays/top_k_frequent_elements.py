"""
Given an integer array nums and an integer k,
return the k most frequent elements.
You may return the answer in any order.

Example 1.
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""

# Main function: Bucket search
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Return k most frequent elements"""

    if len(nums) == 0 or k == 0:
        raise Exception("List of numbers cannot be empty, and k must be greater than 0")

    count: dict = {}
    result: list = []
    frequency: list = [[] for i in range(len(nums) + 1)]

    for number in nums:
        count[number] = 1 + count.get(number, 0)

    for n, c in count.items():
        frequency[c].append(n)  # n occurs c number of times

    for i in range(len(frequency) - 1, 0, -1):  # reversed order
        for n in frequency[i]:
            result.append(n)
            if len(result) == k:
                return result


assert top_k_frequent([1, 1, 1, 2, 2, 3], 2) == [1, 2], "Wrong Answer"
assert top_k_frequent([], 1) == Exception, "Wrong Answer"
assert top_k_frequent([1, 1, 1, 2, 2, 3], 0) == Exception, "Wrong Answer"
