class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        n=len(nums)
        start=nums[0]
        end=nums[0]
        s=""
        fin=[]
        for num in nums[1:]:
            if num == end + 1:
                end = num
            else:
                if start == end:
                    fin.append(str(start))
                else:
                    fin.append(f"{start}->{end}")
                start = end = num
                
        if start == end:
            fin.append(str(start))
        else:
            fin.append(f"{start}->{end}")
        return fin
            