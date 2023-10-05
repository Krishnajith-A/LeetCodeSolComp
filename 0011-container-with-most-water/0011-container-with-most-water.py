class Solution:
    def maxArea(self, height: List[int]) -> int:
        pt1=0
        pt2=len(height)-1
        marea=0
        marea=abs(pt1-pt2)*min(height[pt2],height[pt1])
        while pt1<pt2:
            if height[pt1]<height[pt2]:
                pt1+=1
            else:
                pt2-=1
            ar=abs(pt1-pt2)*min(height[pt2],height[pt1])
            marea=max(marea,ar)
        return marea