class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        i=0
        j=len(nums)-1
        while i<=j:
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
            i+=1
            j-=1
        i=0
        j=k-1
        while i<=j:
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
            i+=1
            j-=1
        i=k
        j=len(nums)-1
        while i<=j:
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
            i+=1
            j-=1
        #nums=nums[::-1]
        #nums[:k]=nums[:k][::-1]
        #nums[k:]=nums[k:][::-1]
        