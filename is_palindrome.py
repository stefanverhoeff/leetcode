import re

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return True

        # Ignore case
        s = s.lower()
        
        # Strip non-alpha numerics from the string
        s = re.sub(r'[^a-z0-9]', '', s)
        
        # compare chars both sides
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            
            start += 1
            end -= 1
        
        # If they meet at the end, it's a palindrome
        return True

sol = Solution()

test_cases = [
                'lala',
                'laal',
                '',
                '0P',
                '505',
                'ohhiqihho',
                'A man, a plan, a canal: Panama'
            ]

for test in test_cases:
    result = sol.isPalindrome(test)
    print(test, result)