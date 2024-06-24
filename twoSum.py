"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
"""

"""
Easily solvable using nested loops and comparing -- O(n^2) complexity
Implement a hashmap;
-enumerate the given array
    - on each index, check difference (target - current value on enumeration)
        - if that difference is in map
            return [map[diff], current i]
        -else add that map[current value] = current i  to map
"""

def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in map:
                return [map[diff], idx]
            map[val] = idx
        return