# Group Anagrams
#
# Given an array of strings, group all anagrams together into sublists.
# An anagram is a string with the same characters as another string,
# but possibly in a different order.
#
# Approach:
# Use a dictionary (hash map) where:
#   - Key: sorted tuple of characters in the word
#   - Value: list of words matching that sorted tuple
#
# Example:
#   "act" and "cat" both have sorted tuple ('a','c','t') → same group.
#
# Time complexity: O(n * k log k)  # n = number of words, k = max length of a word
# Space complexity: O(n * k)

from collections import defaultdict

def groupAnagrams(words):
    container = defaultdict(list)
    result = []
    
    for word in words:
        container[tuple(sorted(word))].append(word)
    
    for value in container.values():
        print(value)
        result.append(value)
    
    return result


result = groupAnagrams(["act","pots","tops","cat","stop","hat"])
print(result)