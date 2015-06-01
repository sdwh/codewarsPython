class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        sorted(nums)
        numDict = {}
        for n in nums:
            numDict[n] = numDict.get(n,0) + 1
        return max(numDict.values())

test = Solution()
print(test.majorityElement([1,2,3,4,4,4,5,7,7,7,4,7]))