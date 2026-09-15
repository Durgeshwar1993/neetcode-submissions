class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        non_alnum_chars = ''.join([c.lower() for c in s if  c.isalnum()])

        i = 0
        j = len(non_alnum_chars)-1


        while i <= j:
            if non_alnum_chars[i] == non_alnum_chars[j]:
                i += 1
                j -= 1
            else:
                return False
        
        return True
        