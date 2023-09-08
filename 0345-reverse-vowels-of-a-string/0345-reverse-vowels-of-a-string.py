class Solution:
    def reverseVowels(self, s: str) -> str:
        a=list(s)
        vow=['a','e','i','o','u','A','E','I','O','U']
        p1=0
        p2=len(s)-1
        while p1<p2:
            while p1<p2 and a[p1] not in vow:
                p1+=1
            while p1<p2 and a[p2] not in vow:
                p2-=1
            a[p1],a[p2]=a[p2],a[p1]
            p1+=1
            p2-=1
        return''.join(a)
            
        