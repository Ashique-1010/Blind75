
"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Tried logics:
1. Iterate through the list of strings
    - compare each strings and check if they are anagrams, add to a list t group anagrams
    - add the grouped anagrams to a list and return
    ==> This logic executes in a time complexity of O((2*n) + n^2) == TLE occurs for this code

"""
"""
def groupAnagrams(strs: list[str]) -> list[list[str]]:
        
    def isAnagram(str1, str2):
        if len(str1) != len(str2):
            return False
        (g1, g2) = ({}, {})
        for i in range(len(str1)):
            g1[str1[i]] = 1 + g1.get(str1[i], 0)
            g2[str2[i]] = 1 + g2.get(str2[i], 0)
        for j in g1:
            if g1[j] != g2.get(j, 0):
                return False
        else:
            return True
        
    anagroups = []
    
    for i in strs:
        temp = []
        for j in strs:
            if isAnagram(i, j)==True:
                #temp.append(i)
                temp.append(j)
        if temp not in anagroups:
            anagroups.append(temp)
    #anagroups = list({g for g in anagroups})
    return anagroups 
"""

"""
2. Using Hashmap
 - create a hashmap using defaultdict with list as factory (value type)
    - for each string in wordslist
        - intialize a hashmap for character count for the string ?
        - initialize a list of length 26 with 0
        - map the count of each characters with zero indexed letters
        - update the count list which reflects how many times each letter appears in the string.
        - convert the count list to a tuple (because lists can't be used as dictionary keys) and use it as a key in the res dictionary.
        - append the string s to the list associated with this key. 
        This groups the string with other strings that have the same character count.
        - we return the values of the res dictionary, which are lists of anagrams.
"""

from collections import defaultdict

def groupAnagrams(strs : list[str]) ->list[list[str]]:
    res = defaultdict(list)

    for s in strs:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord("a")] += 1

        res[tuple(count)].append(s)
    
    return res.values()

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))