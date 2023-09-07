class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1=0
        rob2=0
        for i in nums:
            maxrob=max(i+rob1,rob2)
            rob1=rob2
            rob2=maxrob
        return maxrob
