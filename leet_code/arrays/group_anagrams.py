"""
Given an array of strings strs, group the anagrams together.
You can return the answer in any order. 

An Anagram is a word or phrase formed by rearranging the
letters of a different word or phrase, typically using all
the original letters exactly once.

Example 1.
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""
from collections import defaultdict

test_input = ["eat", "tea", "tan", "ate", "nat", "bat"]
test_output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]


def group_anagrams(strs: list[str]):
    """Group anagrams and return them as a list"""

    result: dict = defaultdict(list)

    for word in strs:
        alph_list = [0] * 26

        for letter in word:
            alph_list[ord(letter) - ord("a")] += 1

        if tuple(alph_list) in result:
            result[tuple(alph_list)].append(word)

        else:
            result[tuple(alph_list)] = [word]

    return result.values()


# Test:
print(group_anagrams(test_input))
