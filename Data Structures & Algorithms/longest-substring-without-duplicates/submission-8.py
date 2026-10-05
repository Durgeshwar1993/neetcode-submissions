class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        d = {}
        length = 0
        k = 0
        for i , j in enumerate(s):
            #print(i,j)
            if j in d and d[j] >= k:
                k = d[j] + 1
            d[j] = i
            length = max(length, i - k + 1)

        return length