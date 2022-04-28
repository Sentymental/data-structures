"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word
or phrase, typically using all the original letters exactly once.
"""

# Main Function
def anagram(s: str, t: str) -> bool:
    """Check if s and t are anagrams"""

    if len(s) != len(t) or (len(s) and len(t)) == 0:
        return False

    hashmap_s: dict = {}
    hashmap_t: dict = {}

    for i, j in zip(s, t):
        hashmap_s[i] = 1 + hashmap_s.get(i, 0)
        hashmap_t[j] = 1 + hashmap_t.get(j, 0)

    for i in hashmap_s:
        if hashmap_s[i] != hashmap_t.get(i, 0):
            return False

    return True


# Tests:
assert anagram("anagram", "margana") == True, "Wrong Answer"
assert anagram("cat", "car") == False, "Wrong Answer"
assert anagram("cat", "anagram") == False, "Wrong Answer"
assert anagram("", "") == False, "Wrong Answer"
