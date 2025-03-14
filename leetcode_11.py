## Problem url: https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            area = width * h

            if max_area < area:
                max_area = area
            
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1

        return max_area
            
