class Solution:
    def func(self,nn):
        if nn == 0 or nn==1:
            return nn
        return self.func(nn-1) + self.func(nn-2)
    def fib(self, n: int) -> int:
        ans = self.func(n)
        return ans
        