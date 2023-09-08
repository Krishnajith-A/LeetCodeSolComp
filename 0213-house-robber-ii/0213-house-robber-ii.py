class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.fn(nums[1:]),self.fn(nums[:-1]))
        
    def fn(self,nums):
        r1,r2=0,0
        maxrob=0
        for i in nums:
            maxrob=max(i+r1,r2)
            r1=r2
            r2=maxrob
        return maxrob