class Solution:
    def reverseVowels(self, s: str) -> str:
        a=list(s)
        vow='aeiouAEIOU'
        p1=0
        p2=len(s)-1
        while p1<p2:
            if a[p1] in vow and a[p2] in vow:
                a[p1],a[p2]=a[p2],a[p1]
                p1+=1
                p2-=1
            elif a[p1] not in vow:
                p1+=1
            elif a[p2] not in vow:
                p2-=1
        return ''.join(a)
            
        