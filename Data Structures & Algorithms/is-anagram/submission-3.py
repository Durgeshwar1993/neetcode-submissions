class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        d = {}
        count = 0
        if len(s) != len(t):
            return False
        for i in s:
            if ord(i) in d:
                d[ord(i)] += 1
            else:
                d[ord(i)] = 1
        for j in t :
            if ord(j) in d:
                d[ord(j)] -= 1
                if  d[ord(j)] < 0:
                    return False
        
        values = sum(d.values())
        print(d)
        if values > 0:
            return False
        return True
        