class Solution:
    def climbStairs(self, n: int) -> int:
        # memo=[-1]*(n+1)
        # memo[0]=1
        # memo[1]=1
        # for i in range(2,n+1):
        #     memo[i]=memo[i-1]+memo[i-2]
        # return memo[n]
        p1=1
        p2=1
        p3=0
        if n==1: return 1
        for i in range(2,n+1):
            p3=p1+p2
            p1=p2
            p2=p3
        return p3
        