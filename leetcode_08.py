## If you want to check the description of the challenge, check: https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        sign = ''
        number = ['0','1','2','3','4','5','6','7','8','9']
        result = ''
        flag_not_first_num = False
        flag_existing_sign = False
        
        i = 0
        n = len(s)
        
        while i < n and s[i] == ' ':
            i += 1
        
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = s[i]
            i += 1
        
        while i < n and s[i] in number:
            if s[i] == '0' and not flag_not_first_num:
                i += 1
                continue
            flag_not_first_num = True
            result += s[i]
            i += 1
        
        if not result:
            return 0
        
        if sign == '-':
            result = -int(result)
        else:
            result = int(result)
        
        if result > 2147483647:
            return 2147483647
        elif result < -2147483648:
            return -2147483648
        
        return result
