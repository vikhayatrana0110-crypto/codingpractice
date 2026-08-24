class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        m_p = 0
        min_p = float("inf")
        for i in range(0,n):
            min_p = min(prices[i],min_p)
            m_p = max(m_p,prices[i]-min_p)

           
        return m_p
        