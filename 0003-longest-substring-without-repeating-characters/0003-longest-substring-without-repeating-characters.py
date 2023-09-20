class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        beg=0
        dict1={}
        for end in range(len(s)):
            if s[end] in dict1 and dict1[s[end]]>=beg:
                beg=dict1[s[end]]+1
            dict1[s[end]]=end
            curr=end-beg+1
            maxlen=max(maxlen,curr)

        return maxlen
                
            
                
        
            