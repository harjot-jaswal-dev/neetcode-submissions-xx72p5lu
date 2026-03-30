class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        L, R = 0, len(s) - 1

        while L < R:
            letter_l, letter_r = s[L].lower(), s[R].lower()
            if not letter_l.isalnum():
                L += 1
                continue
            elif not letter_r.isalnum():
                R -= 1
                continue
            elif letter_l != letter_r:
                return False
            L += 1
            R -= 1
        return True