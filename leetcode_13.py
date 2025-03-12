## Problem url: https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
    
        number = 0
        for index, letter in enumerate(s):
            if letter == 'I':
                if index+1 == len(s):
                    number += roman_dict[letter]
                    continue
                if s[index+1] == 'V':
                    number += 4
                    continue
                if s[index+1] == 'X':
                    number += 9
                    continue
            if letter == 'V' and s[index-1] == 'I':
                continue
            if letter == 'X' and s[index-1] == 'I':
                continue
            if letter == 'X':
                if index+1 == len(s):
                    number += roman_dict[letter]
                    continue
                if s[index+1] == 'L':
                    number += 40
                    continue
                if s[index+1] == 'C':
                    number += 90
                    continue
            if letter == 'L' and s[index-1] == 'X':
                continue
            if letter == 'C' and s[index-1] == 'X':
                continue
            if letter == 'C':
                if index+1 == len(s):
                    number += roman_dict[letter]
                    continue
                if s[index+1] == 'D':
                    number += 400
                    continue
                if s[index+1] == 'M':
                    number += 900
                    continue
            if letter == 'D' and s[index-1] == 'C':
                continue
            if letter == 'M' and s[index-1] == 'C':
                continue
            if letter in roman_dict:
                number += roman_dict[letter]
    
        return number

## Generalized solution

class Solution:
    def romanToInt(s: str) -> int:
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        n = len(s)
        for i in range(n):
            if i < n - 1 and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                total -= roman_to_int[s[i]]
            else:
                total += roman_to_int[s[i]]
        return total
