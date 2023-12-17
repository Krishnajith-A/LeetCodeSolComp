class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        dig={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        def f(i,cur):
            if len(cur)==len(digits):
                res.append(cur)
                return
            for j in dig[digits[i]]:
                f(i+1,cur+j)
        if digits:
            f(0,'')
        return res
            
            
        