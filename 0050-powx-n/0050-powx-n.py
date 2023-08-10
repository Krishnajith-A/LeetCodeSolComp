class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        elif n<0:
            n=-n
            x=1/x
        r=1
        while(n>0):
            if n%2==1:
                r*=x
            x*=x
            n=n//2
        
        return r