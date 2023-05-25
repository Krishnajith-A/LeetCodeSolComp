'''Question: Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prepro=[1]*len(nums)
        sufpro=[1]*len(nums)
        for i in range(1, len(nums)):
            prepro[i] = nums[i - 1] * prepro[i - 1]
        for i in range(len(nums)-2,-1,-1):
            sufpro[i]=nums[i+1]*sufpro[i+1]
        print(sufpro,prepro)
        for i in range(len(nums)):
            prepro[i]=prepro[i]*sufpro[i]
        return(prepro)