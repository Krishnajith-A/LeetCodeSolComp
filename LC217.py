'''Question :Given an integer array nums, return true if any value 
appears at least twice in the array, and return false if every element is distinct.

 '''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict={}
        for i in nums:
            if i in dict:
                return True
            else:
                dict[i]=1
        return False