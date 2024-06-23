"""To check if an array contains duplicate elements"""

"""1. Create a hash map of the array with elements.
        If element already contains, then return true."""

def containsDuplicate(nums):
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)
        return False


arr = [0,1,2,3,0]
print(containsDuplicate(arr))

        