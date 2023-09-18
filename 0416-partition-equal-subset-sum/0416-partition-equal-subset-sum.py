class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        dp=set()
        dp.add(0)
        t=sum(nums)/2
        for i in range(len(nums)):
            newdp=set()
            for j in dp:
                if j+nums[i]==t:
                    return True
                newdp.add(j+nums[i])
                newdp.add(j)
            dp=newdp
        return True if t in dp else False