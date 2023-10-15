class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for i in nums:
            if i in dic.keys():
                dic[i]+=1
            else:
                dic[i]=1
        f=[[]for i in range(len(nums)+1)]
        for n,c in dic.items():
            f[c].append(n)
        res=[]
        for i in range(len(f)-1,0,-1):
            for n in f[i]:
                res.append(n)
                if len(res)==k:
                    return res
            

            
        
        