## For the description of the problem, check this link: https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list_ordered = nums1 + nums2
        list_ordered.sort()
        length = len(list_ordered)

        if length % 2 == 0:
            middle_right = length // 2
            middle_left = middle_right - 1
            median = (list_ordered[middle_left] + list_ordered[middle_right]) / 2
        else:
            middle = length // 2
            median = list_ordered[middle]

        return median
