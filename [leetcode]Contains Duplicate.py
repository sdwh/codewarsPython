class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        res = None
        for n in sorted(nums):
            if n == res:
                return True
            else:
                res = n
        return False                
