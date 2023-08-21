class Solution:
    def romanToInt(self, s: str) -> int:
        vals={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res=0
        prev_val=0
        for i in range(len(s)-1,-1,-1):
            cur=vals[s[i]]
            if cur<prev_val:
                res-=cur
            else:
                res+=cur
            prev_val=cur
        return res