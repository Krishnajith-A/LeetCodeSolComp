class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        maxp=0
        for i in range(n):
            if i>maxp:
                return False
            maxp=max(maxp,nums[i]+i)
            if maxp>=n-1:
                return True
        return False