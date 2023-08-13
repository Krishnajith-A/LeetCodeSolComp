class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ml=min(len(s) for s in strs)
        for i in range(ml):
            c=strs[0][i]
            if all(s[i]==c for s in strs):
                continue
            else:
                return strs[0][:i]
        return strs[0][:ml]
            