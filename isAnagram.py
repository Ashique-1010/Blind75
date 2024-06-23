"""
Check if two strings are anagrams

Tried logics: 
1. Converted each characters in ascii and compared sum
    if both strings have same letters in same count -- they will have equal sums
    logic is wrong because different letters can sum upto same value with different ascii values

2. Created hashmap for each string with their counts
    -- compare sount value for same character in both hashmaps -- worked.
"""

def isAnagram(s, t):
    if len(s) != len(t):
            return False
    (sset, tset) = ({}, {})
    for i in range(len(s)):
        sset[s[i]] = 1 + sset.get(s[i], 0)
        tset[t[i]] = 1 + tset.get(t[i], 0)
# if the character doesnt exist yet the function returns a keyerror so we can use  get function
# get function returns the value of the key, if it doesnt exist in dictionary, returns 0
#       sset.update({s[i]:s.count(s[i])}) --> this is another way which will throw error
#       tset.update({t[i]:t.count(t[i])}) 
# So we use the get function again here    
    for j in sset:
        if sset[j] != tset.get(j, 0):
             return False
    else:
        return True
    
isAnagram("anagram", "nagaram")