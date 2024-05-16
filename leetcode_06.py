## If interested, you can find the problem here: https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = [""] * numRows
        row_number = 0
        direction = 1      
 
        for i in range(len(s)):
            result[row_number] = result[row_number] + s[i]
            if row_number < numRows - 1 and direction == 1:
                row_number += 1
            elif row_number > 0 and direction == -1:
                row_number -= 1
            else:
                direction *= -1
                row_number += direction
 
        return ''.join(result)
            
