## For the description of the problem, check this link: https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        num_reversed = 0
        flag_invert = False
        
        if x < 0:
            x = -x
            flag_invert = True
        
        while x > 0:
            rest_num = x % 10
            num_reversed = num_reversed * 10 + rest_num
            x = x // 10
        
        if flag_invert:
            num_reversed = -num_reversed
        
        if num_reversed < -2**31 or num_reversed > 2**31 - 1:
            return 0
        
        return num_reversed
