# Valid Anagram

# Given two strings s and t, return true if the two strings are anagrams of
#  each other, otherwise return false.

# An anagram is a string that contains the exact same characters as 
# another string, but the order of the characters can be different.

# How to solve this problem, the optimal solution is make a dict for each word
# and then make a comparison if both of them are equal that means are anagrams but otherwise are differents

# Time complexity : Big O(N)
# Space complexity : Big O(N)

def isAnagram(s, t):
        dict_s = {}
        dict_t = {}

        for letter in s:
            if letter in dict_s:
                dict_s[letter] += 1
            else:
                dict_s[letter] = 1
        

        for letter in t:
            if letter in dict_t:
                dict_t[letter] += 1
            else:
                dict_t[letter] = 1
        
        if dict_s == dict_t:
            return True
        else:
            return False
        

result = isAnagram("racecar", "carrace")

print(result)
