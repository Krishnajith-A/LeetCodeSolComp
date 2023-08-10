class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        w=s.split()
        dic_1={}
        dic_2={}        
        if len(pattern)!=len(w):
            return False
        for i,j in zip(pattern,w):
            if i not in dic_1 and j not in dic_2:
                dic_1[i]=j
                dic_2[j]=i
            else:
                if i in dic_1 and dic_1[i]!=j:
                    return False
                elif j in dic_2 and dic_2[j]!=i:
                    return False
        return True
    