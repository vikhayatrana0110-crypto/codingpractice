class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer= [1] * n
        l_p=1
        for i in range(n):
            answer[i]=l_p
            l_p*=nums[i]
        r_p=1
        for i in range(n-1,-1,-1):
            answer[i]*=r_p
            r_p*=nums[i]
        return answer

        