class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [None for _ in range(n + 1)]
        power = 1

        for i in range(n + 1):
            if i == 0:
                ans[i] = 0
            elif i == power:
                ans[i] = 1
            elif i == power * 2:
                ans[i] = 1
                power *= 2
            elif i > power:
                if ans[i - power] is not None:
                    ans[i] = ans[i - power] + 1
            
        
        return ans

        