class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1=0
        p2=len(numbers)-1
        lis=[p1,p2]
        while p1<p2:
            if numbers[p2]+numbers[p1]<target:
                p1+=1
            elif numbers[p2]+numbers[p1]==target:
                lis[0]=p1
                lis[1]=p2
                break
            elif numbers[p1]+numbers[p2]>target:
                p2-=1
                p1=0
        lis[0]+=1
        lis[1]+=1
        return lis

