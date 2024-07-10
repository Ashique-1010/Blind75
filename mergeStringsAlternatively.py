"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

"""
"""
Logics:
1. Initialise array for storing merged string
   - get min length of two strings
   - initialise a pointer to alternatively get string indexes
   - iterate till min length
   - after adding character from first word, update pointer, add character from second string
   - On completion of iteration, slice the longer word with remaining index length and add to merged string.

"""

def mergeAlternately1(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        l1 = len(word1)
        l2 = len(word2)
        merged = [""]*(l1 + l2)
        k = 0
        if l1 >= l2:
            for i in range(l2):
                merged[k] = word1[i]
                k += 1
                merged[k] = word2[i]
                k += 1
            merged_part = ''.join(c for c in merged)
            merged_final = merged_part + word1[k-l2:]
            return merged_final
        else:
            for i in range(l1):
                merged[k] = word1[i]
                k += 1
                merged[k] = word2[i]
                k += 1
            merged_part = ''.join(c for c in merged)
            merged_final = merged_part + word2[k-l1:]
            return merged_final

"""Not so Optimized version, But smaller version"""

def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged_string = []
        l1, l2 = len(word1), len(word2)
        min_len = min(l1, l2)

        # Add alternating characters from both words up to the length of the shorter word
        for i in range(min_len):
             merged_string.append(word1[i])
             merged_string.append(word2[i])
        
        # Add remaining characters from the longer word
        if l1 > l2:
             merged_string.extend(word1[min_len:])
        else:
             merged_string.extend(word2[min_len:])
        
        # Convert to string
        return "".join(merged_string)