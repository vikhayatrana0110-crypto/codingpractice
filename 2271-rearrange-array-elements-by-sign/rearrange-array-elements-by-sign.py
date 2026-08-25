class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        P_I,N_I=0,1
        for i in range(0,n):
            if nums[i]>=0:
                result[P_I]=nums[i]
                P_I +=2
            else:
                result[N_I]=nums[i]
                N_I +=2
        return result