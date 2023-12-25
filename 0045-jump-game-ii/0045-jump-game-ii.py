class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        jumps=0  
        mr=nums[0] 
        steps=nums[0]  
        for i in range(1, n - 1): 
            mr=max(mr, i + nums[i])
            steps-=1
            if steps==0:
                jumps+=1
                steps=mr-i
        return jumps+1 