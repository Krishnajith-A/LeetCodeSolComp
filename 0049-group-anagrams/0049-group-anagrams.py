class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for i in strs:
            sig=''.join(sorted(i))
            if sig not in dic:
                dic[sig]=[i]
            else:
                dic[sig].append(i)
        res=list(dic.values())
        return res
                    


            