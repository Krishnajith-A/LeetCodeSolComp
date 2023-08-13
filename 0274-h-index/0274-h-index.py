class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n=len(citations)
        left=0
        right=n-1
        h=0
        while left<=right:
            mid=(left+right)//2
            if citations[mid]>=n-mid:
                h=n-mid
                right=mid-1
            else:
                left=mid+1
        return h
        
                
            