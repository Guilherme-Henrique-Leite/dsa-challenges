# 125. Valid Palindrome
s = "A man, a plan, a canal: Panama"

def isPalindrome(self, s: str) -> bool:
        def is_alnum(c):
            return ('A' <= c <= 'Z') or ('a' <= c <= 'z') or ('0' <= c <= '9')

        def to_lower(c):
            if 'A' <= c <= 'Z':
                return chr(ord(c) + 32)
            return c

        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not is_alnum(s[left]):
                left += 1
            while left < right and not is_alnum(s[right]):
                right -= 1
            if to_lower(s[left]) != to_lower(s[right]):
                return False
            left += 1
            right -= 1

        return True


isPalindrome(s=s)