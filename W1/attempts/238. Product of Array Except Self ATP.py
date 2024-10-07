#238. Product of Array Except Self
#https://leetcode.com/problems/product-of-array-except-self/description/
#参考solution ‘Simple and easy 1 min explanation in Python and JAVA’

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lp=1
        rp=1
        i=0
        pes=[1]*len(nums)
        while i < len(nums):
            lp *= nums[i]
            rp *= nums[-i]
            pes[i] *= lp
            pes[-i] *= rp
            i += 1
        return pes