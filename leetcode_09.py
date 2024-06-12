## Problem url: https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        string_int = str(x)
        string_reversed = string_int[::-1]
        
        return int(string_reversed) == x

## Without converting to string

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        original_x = x
        digits = []
        
        while x > 0:
            digit = x % 10
            digits.append(digit)
            x = x // 10
        
        num_end = 0
        for digit in digits:
            num_end = num_end * 10 + digit

        return num_end == original_x
