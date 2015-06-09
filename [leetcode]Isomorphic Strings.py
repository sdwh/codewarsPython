class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        def isomorphic(s,t):
            d = {}
            for k,v in zip(s,t):
                d[k] = v
            return ''.join([d[c] for c in s]) == t
        return isomorphic(s,t) and isomorphic(t,s)

test = Solution()
print(test.isIsomorphic('ab','aa'))
print(test.isIsomorphic('egg','add'))
print(test.isIsomorphic('egg','adv'))
print(test.isIsomorphic('paper','title'))
print(test.isIsomorphic('paper','title'))