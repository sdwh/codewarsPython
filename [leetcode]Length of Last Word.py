class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        num = 0
        s = s.strip()
        for c in s[::-1]:
            if c == ' ':
                break
            num += 1
        return num

test = Solution()
print(test.lengthOfLastWord('H '))