class Solution:
    def climbStairs(self, n: int) -> int:
        a=1
        b=1
        c=0
        if n==0:
            return 0
        elif n==1:
            return 1
        for i in range(0,n-1):
            c=a+b
            a=b
            b=c
        return c