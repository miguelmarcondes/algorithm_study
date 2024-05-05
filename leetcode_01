## For the description of the problem, check this link: https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for first_index, first_num in enumerate(nums):
            for sec_ind in range(first_index + 1, len(nums)):
                if first_num + nums[sec_ind] == target:
                    return [first_index, sec_ind]
        return None
    
## Solution less than O(n^2) time complexity
class Solution_2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], index]
            num_dict[num] = index
        return None
