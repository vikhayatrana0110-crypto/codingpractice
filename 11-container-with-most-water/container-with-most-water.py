class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        res=0
        l,r=0,n-1
        while l<r:
            area = (r-l) * min(height[l],height[r])
            res = max(res,area)
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return res
