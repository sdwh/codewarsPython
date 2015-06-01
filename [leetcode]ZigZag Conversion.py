class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        contain = [[] for __ in range(numRows)]
        trans = tuple(range(numRows)) + tuple(range(numRows-1)[::-1])
        shift = (numRows - 1) * 2 if numRows > 1 else 1
        for i in range(len(s)):
            contain[trans[i%shift]].append(s[i])
        return ''.join([''.join(con) for con in contain])

test = Solution()
print(test.convert("PAYPALISHIRING", 3))
print(test.convert("ABCD", 1))