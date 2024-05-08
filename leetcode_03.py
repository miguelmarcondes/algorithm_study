## For the description of the problem, check this link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: ## checking for empty strings
            return 0
        
        substring_list = []
        counter = 0
        while counter < len(s):
            string = s[counter::]
            substring = ''
            for letter in string:
                if letter in substring:
                    break
                substring += letter
            substring_list.append(substring)
            counter += 1
        
        longest_substring = max(substring_list, key=len)
        
        return len(longest_substring)
            
