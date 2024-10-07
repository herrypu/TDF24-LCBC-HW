#75. Sort Colors
#https://leetcode.com/problems/sort-colors/description/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l=0
        r=1
        while l < r:
            r=len(nums)-l-1
            if nums[l]>nums[r]:
                temp=nums[l]
                nums[l]=nums[r]
                nums[r]=temp
            l += 1